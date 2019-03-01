#!/usr/bin/env python

import argparse


def app(_str):
    res = list()
    start, end = 0, 0

    while end < len(_str):
        if _str[end] not in _str[start:end]:
            end += 1
        else:
            start += 1

        if start == end:
            end += 1

        if len(_str[start:end]) > len(res):
            res = _str[start:end]

    print(res)


def main():
    parser = argparse.ArgumentParser(description='MHomeWork app')

    parser.add_argument('string', default="", type=str, help='Input string')

    args = parser.parse_args()

    if 'func' in args:
        args.func()
    else:
        app(args.string)


if __name__ == '__main__':
    main()
