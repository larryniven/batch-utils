#!/usr/bin/env python3

import sys

def read_batch(f):
    lines = []
    line = f.readline()
    while line != '.\n':
        lines.append(line)
        line = f.readline()
    lines.append(line)
    return lines

for line in sys.stdin:
    key, value = line.split()

    filename, shift = value.split(':')

    f = open(filename)
    f.seek(int(shift))

    lines = read_batch(f)

    for line in lines:
        print(line, end='')

