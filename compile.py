#!/usr/bin/env python

import argparse

ap = argparse.ArgumentParser()
ap.add_argument('--en2cn', action='store_true', default=False)
ap.add_argument('input', type=argparse.FileType('r'))
ap.add_argument('output', type=argparse.FileType('w'))
args = ap.parse_args()

@eval('lambda x: x()')
def res():
    with open('table.txt') as f:
        res = {}
        for x in f.readlines():
            try:
                cn, en = x.split()
            except ValueError:
                pass
            if args.en2cn:
                res[en] = cn
            else:
                res[cn] = en
        return res


ident = ''
instring = ''
for c in args.input.read():
    if c == '"' or c == "'":
        instring = c
    if instring and c != instring:
        args.output.write(c)
        continue
    if c.isidentifier():
        ident += c
    else:
        if ident:
            args.output.write(res.get(ident, ident))
            ident = ''
        args.output.write(c)