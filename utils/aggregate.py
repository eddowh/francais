# -*- coding: utf-8 -*-

import os

def aggregate_md_files(folder, levels):

    # aggregate everything
    content = [
        "# {title}\n\n{body}\n\n".format(
            title=level['title'],
            body=open(
                os.path.join(folder, level['filename'] + '.md'), 'rt'
            ).read()
        )
        for level in levels
    ]
    content = "".join(content)

    # remove the two blank lines at the end
    content = content[:-2]

    return content
