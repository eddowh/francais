#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

FOLDER = os.path.dirname(os.path.realpath(__file__))

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
)


def main():

    # aggregate everything
    content = [
        "# {title}\n\n{body}\n\n".format(
            title=level['title'],
            body=open(
                os.path.join(FOLDER, level['filename'] + '.md'), 'rt'
            ).read()
        )
        for level in LEVELS
    ]
    content = "".join(content)

    # remove the two blank lines at the end
    content = content[:-2]

    # put everything into a file
    with open(os.path.join(FOLDER, 'hacking-fr.md'), 'wt') as outfile:
        outfile.write(content)

    return

if __name__ == '__main__':
    main()
