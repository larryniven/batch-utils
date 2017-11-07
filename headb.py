#!/usr/bin/env python3

import sys

count = 0
area = 'head'
for line in sys.stdin:
    if count < int(sys.argv[1]):
        print(line, end='')
    else:
        break

    if area == 'head':
        area = 'body'

    elif area == 'body' and line == '.\n':
        area = 'head'
        count += 1

    elif area == 'body':
        pass

