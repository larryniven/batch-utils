#!/usr/bin/env python3

import sys

area = 'head'
hit = False

for line in sys.stdin:
    if area == 'head':
        area = 'body'
        name = line.strip()

    elif area == 'body' and line == '.\n':
        area = 'head'
        if hit:
            break

    elif area == 'body':
        if name == sys.argv[1]:
            print(line, end='')
            hit = True

