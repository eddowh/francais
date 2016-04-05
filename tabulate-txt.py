#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Command line tool to convert text files to markdown tables,
given a boundary.
"""

import argparse

from tabulate import tabulate


FILE_EXT = '.txt'
END_PUNCTUATION_MARKS = ('.', '!', '?')


def is_sentence(text):
    return True in map(lambda p: text.endswith(p), END_PUNCTUATION_MARKS)


def capitalize_if_is_sentence(text):
    if is_sentence(text):
        return text[0].upper() + text[1:]
    else:
        return text


def to_markdown_tables(file, headers, boundary):
    contents = file.readlines()
    fr_en_pairs = tuple([
        tuple(map(capitalize_if_is_sentence,
                  [t.strip() for t in fr_en]))
        for fr_en
        in list(map(lambda l: l[:-1].split(boundary), contents))
    ])
    fr_en_pairs = sorted(fr_en_pairs, key=lambda k: k[0])
    return tabulate(fr_en_pairs,
                    # bold column names
                    map(lambda h: '**{}**'.format(h), headers),
                    tablefmt="pipe")


def create_parser():
    """Return command-line parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--recursive", action="store_true",
                        help="Run recrusively over directories")
    parser.add_argument("files", nargs="*",
                        help="Name of input file",
                        type=argparse.FileType('rt'))
    return parser


def parse_args():
    """Parse command-line options."""
    parser = create_parser()
    args = parser.parse_args()
    # check for valid input
    if not args.files:
        parser.error("Incorrect number of arguments.")
    return args


def main():
    """Command-line entry."""
    args = parse_args()
    for file in args.files:
        if file.name.endswith(FILE_EXT):
            with open(file.name[:-len(FILE_EXT)] + '.md', 'wt') as fd:
                fd.write(
                    (to_markdown_tables(
                        file,
                        headers=["français", "english"],
                        boundary="==")
                     )
                )

if __name__ == '__main__':
    main()
