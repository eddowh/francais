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
        "title": "Survival",
        "filename": "survival",
    },
    {
        "title": "Basic Q & A",
        "filename": "basic-QnA",
    },
    {
        "title": "Sounding French",
        "filename": "sounding-french",
    },
    {
        "title": "Nouns and Adjectives",
        "filename": "nouns-and-adjectives",
    },
    {
        "title": "Getting Around",
        "filename": "getting-around",
    },
    {
        "title": "Eating and Drinking",
        "filename": "eating-and-drinking",
    },
    {
        "title": "Family and Work",
        "filename": "family-and-work",
    },
    {
        "title": "Boring but Necessary",
        "filename": "boring-but-necessary",
    },
    {
        "title": "Shopping",
        "filename": "shopping",
    },
    {
        "title": "When Things Go Wrong",
        "filename": "when-things-go-wrong",
    },
    {
        "title": "Accomodation",
        "filename": "accomodation",
    },
)


def main():
    with open(os.path.join(FOLDER, FILENAME + '.md'), 'wt') as outfile:
        outfile.write(aggregate_md_files(FOLDER, LEVELS))
    return

if __name__ == '__main__':
    main()
