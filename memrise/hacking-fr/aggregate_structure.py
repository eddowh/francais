#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import sys

from pathlib import Path

# import from directory
sys.path.insert(1, os.path.abspath(str(Path(__file__).parents[2])))
from utils.aggregate import *

FOLDER = os.path.dirname(os.path.realpath(__file__))
FILENAME = os.path.basename(FOLDER)  # same as folder name

LEVELS = (
    {
        "title": "The Essentials",
        "filename": "essentials",
    },
    {
        "title": "Foundation Vocabulary",
        "filename": "foundation-vocab",
    },
    {
        "title": "French Questions",
        "filename": "questions",
    },
    {
        "title": "At the Market",
        "filename": "at-the-market",
    },
    {
        "title": "Getting Around",
        "filename": "getting-around",
    },
    {
        "title": "At the Restaurant",
        "filename": "at-the-restaurant",
    },
)


def main():
    with open(os.path.join(FOLDER, FILENAME + '.md'), 'wt') as outfile:
        outfile.write(aggregate_md_files(FOLDER, LEVELS))
    return

if __name__ == '__main__':
    main()
