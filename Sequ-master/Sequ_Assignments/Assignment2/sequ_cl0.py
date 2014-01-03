#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#Copyright © 2013 James Beedy
#CS 300 Assignment 2 cl0

import argparse


def main():
    parser = create_parser()
    parser.set_defaults(func=sequ)
    args = parser.parse_args()
    for i in args.func(args):
        print(i)


def sequ(args):
        return range(args.min, args.max + 1)


def create_parser():
    parser = argparse.ArgumentParser(
        description='Sequ',
        prog='SEQU'
    )
    parser.add_argument(
        'min',
        metavar='min',
        help="minimum",
        type=int
    )
    parser.add_argument(
        'max',
        metavar='max',
        help="maximum",
        type=int
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s cl0'
    )
    return parser

if __name__ == '__main__':
    main()
