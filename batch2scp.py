#!/usr/bin/env python3

import sys
import os.path

f = open(sys.argv[1])

idx = f.tell()
line = f.readline()

area = 'head'

while line:
    if area == 'head':
        area = 'body'
        key = line.strip()

    elif area == 'body' and line == '.\n':
        area = 'head'

        print('{} {}:{}'.format(key, sys.argv[1], idx))

        idx = f.tell()

    line = f.readline()
