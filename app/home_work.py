#!/usr/bin/env python

import argparse


def app(_str):
    res = list()
    start, end = 0, 0

    while end < len(_str):
        if _str[end] not in res:
            end += 1
        else:
            start += 1

        if len(_str[start:end]) >= len(res):
            res = _str[start:end]

        if start == end:
            end += 1

    print(res)


def main():
    parser = argparse.ArgumentParser(description='M home work app')

    parser.add_argument('string', default="", type=str, help='Input string')

    args = parser.parse_args()

    if 'func' in args:
        args.func()
    else:
        app(args.string)


if __name__ == '__main__':
    main()
