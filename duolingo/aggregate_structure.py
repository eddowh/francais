#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import sys

from pathlib import Path

# import from directory
sys.path.insert(1, os.path.abspath(str(Path(__file__).parents[1])))
from utils.aggregate import *

FOLDER = os.path.dirname(os.path.realpath(__file__))
FILENAME = os.path.basename(FOLDER)  # same as folder name

LEVELS = (
    {
        "title": "Basics",
        "filename": "levels/basics",
    },
    {
        "title": "Phrases",
        "filename": "levels/phrases",
    },
    {
        "title": "Food",
        "filename": "levels/food",
    },
    {
        "title": "Animals",
        "filename": "levels/animals",
    },
    {
        "title": "Adjectives",
        "filename": "levels/adjectives",
    },
    {
        "title": "Plurals",
        "filename": "levels/plurals",
    },
)


def main():
    with open(os.path.join(FOLDER, FILENAME + '.md'), 'wt') as outfile:
        outfile.write(aggregate_md_files(FOLDER, LEVELS))
    return

if __name__ == '__main__':
    main()
