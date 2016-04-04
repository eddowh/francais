#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Command line tool to convert text files to markdown tables,
given a boundary.
"""

import argparse

from tabulate import tabulate


FILE_EXT = '.txt'


def to_markdown_tables(file, headers, boundary):
    contents = file.readlines()
    fr_en_pairs = tuple([
        (fr.strip(), en.strip())
        for fr, en
        in list(map(lambda l: l[:-1].split(boundary), contents))
    ])
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
