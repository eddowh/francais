#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Command line tool to convert text files to markdown tables,
given a boundary.
"""

from pprint import pprint
import argparse
import os

from tabulate import tabulate


FILE_EXT = '.txt'
END_PUNCTUATION_MARKS = ('.', '!', '?')


def remove_duplicates(seq):
    """Remove duplicates from a list while preserving order.

    Courtesy of StackOverflow user < Markus Jarderot >.
    """
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def is_sentence(text):
    return True in map(lambda p: text.endswith(p), END_PUNCTUATION_MARKS)


def capitalize_if_is_sentence(text):
    if is_sentence(text):
        return text[0].upper() + text[1:]
    else:
        return text


def to_markdown_tables(file, headers, boundary,
                       separate_words_and_phrases=False):
    contents = file.readlines()
    fr_en_pairs = tuple([
        tuple(map(capitalize_if_is_sentence,    # capitalize if is sentence
                  [t.strip() for t in fr_en]))  # strip whitespace
        for fr_en
        in list(map(lambda l: l[:-1].split(boundary), contents))
    ])
    fr_en_pairs = sorted(fr_en_pairs, key=lambda k: k[0])
    if separate_words_and_phrases:
        res = (
            "# Sentences\n\n"
            + tabulate(filter(lambda x: x[0][0].isupper() or is_sentence(x[0]), fr_en_pairs),
                       map(lambda h: '**{}**'.format(h), headers),
                       tablefmt="pipe")
            + "\n\n# Words & Phrases\n\n"
            + tabulate(filter(lambda x: not (x[0][0].isupper() or is_sentence(x[0])), fr_en_pairs),
                       map(lambda h: '**{}**'.format(h), headers),
                       tablefmt="pipe")
        )
    else:
        res = tabulate(fr_en_pairs,
                       map(lambda h: '**{}**'.format(h), headers),
                       tablefmt="pipe")
    return res


def list_all_files(in_path, omit_hidden=True):
    res = []
    for dir_path, subdir_list, file_list in os.walk(in_path):
        for fname in file_list:
            full_path = os.path.join(dir_path, fname)
            if omit_hidden:
                if (full_path.startswith(os.path.join(in_path, '.')) or
                    os.path.basename(full_path).startswith('.')):
                    continue
            res.append(os.path.abspath(full_path))
    return tuple(res)


def create_parser():
    """Return command-line parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--recursive", action="store_true",
                        help="run recursively over directories")
    parser.add_argument("--categorize", action="store_true",
                        help="categorize to words/phrases and sentences")
    parser.add_argument("fd", nargs="*",
                        help="name of input file or directory")
    return parser


def parse_args():
    """Parse command-line options."""
    parser = create_parser()
    args = parser.parse_args()

    # check for valid input
    if not args.fd:
        parser.error("Incorrect number of arguments.")

    # recursive?
    if not args.recursive:
        first_dir = next((fd for fd in args.fd if os.path.isdir(fd)), None)
        if first_dir is not None:
            raise IsADirectoryError(first_dir)

    return args


def main():
    """Command-line entry."""
    args = parse_args()

    # get all the files
    all_files = []
    for fd in sorted(args.fd):
        if os.path.isfile(fd):
            all_files.append(os.path.abspath(fd))
        else:
            all_files.extend(list_all_files(fd))
    # filter out files without .txt extension
    dir_path = os.path.abspath('.')
    all_text_files = tuple([
        os.path.relpath(f, dir_path)
        for f
        in filter(lambda x: x.endswith(FILE_EXT),
                  remove_duplicates(all_files))
    ])

    # convert all to markdown!
    for tf in all_text_files:
        with open(tf[:-len(FILE_EXT)] + '.md', 'wt') as outfile:
            outfile.write(
                to_markdown_tables(
                    open(tf, 'rt'),
                    headers=["Français", "English"],
                    boundary="==",
                    separate_words_and_phrases=args.categorize
                )
            )

if __name__ == '__main__':
    main()
