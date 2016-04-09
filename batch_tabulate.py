#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from glob import glob
import os
import yaml

TABULATE_SCRIPT = 'tabulate_txt.py'
AGGREGATE_SCRIPT = 'aggregate_structure.py'
CONFIG_FILE = '.tab.yml'
CONFIG = yaml.load(open(CONFIG_FILE).read())


def main():
    for folder in CONFIG:

        all_files = glob(os.path.join(folder, '*.txt'))

        to_be_categorized = CONFIG[folder]['categorize']
        if to_be_categorized:
            to_be_categorized = [
                os.path.join(folder, file + '.txt')
                for file in to_be_categorized
            ]
            for file in to_be_categorized:
                all_files.remove(file)

        to_be_excluded = CONFIG[folder]['exclude']
        if to_be_excluded:
            to_be_excluded = [
                os.path.join(folder, file + '.txt')
                for file in to_be_excluded
            ]
            for file in to_be_excluded:
                all_files.remove(file)

        # commands
        if all_files:
            command = "python {script} {input}".format(
                script=TABULATE_SCRIPT,
                input=" ".join(all_files)
            )
            os.popen(command)
        if to_be_categorized:
            command = "python {script} {args} {input}".format(
                script=TABULATE_SCRIPT,
                args="--categorize",
                input=" ".join(to_be_categorized)
            )
            os.popen(command)

        # nested folder with subsections
        if '/' in folder:
            command = "python {script}".format(
                script=os.path.join(folder, AGGREGATE_SCRIPT)
            )
            os.popen(command)

if __name__ == '__main__':
    main()
