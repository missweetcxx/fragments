#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple
from os import path

from config import ROOT_PATH

STAT = namedtuple("STAT", ["blanks", "comments", "codes"])
FILE_PATH = path.join(ROOT_PATH, 'fragments/triangle.py')


def code_stat(path):
    comments = blanks = codes = 0
    is_multiple_comment = False
    with open(path, encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()

            # single comments
            if line.startswith('#'):
                comments += 1
            elif (line.startswith("'''") and line.endswith("'''") and len(line) > 3) or \
                    (line.startswith('"""') and line.endswith('"""') and len(line) > 3):
                comments += 1

            # multi-line comments
            elif line.startswith("'''") or line.startswith('"""'):
                comments += 1
                is_multiple_comment = not is_multiple_comment
            elif is_multiple_comment:
                comments += 1

            # blanks
            elif len(line) == 0:
                blanks += 1

            # codes
            else:
                codes += 1

    return {"comments": comments, "blanks": blanks, "codes": codes}


if __name__ == '__main__':
    print(code_stat(FILE_PATH))
