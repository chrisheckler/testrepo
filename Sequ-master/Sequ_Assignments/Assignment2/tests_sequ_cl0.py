#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#Copyright © 2013 James Beedy
#CS 300 Assignment2 cl0
import unittest
import doctest
import argparse
import epydoc

#implemented function based structure


def sequ(args):
    """
    usage: tests_sequ_cl0.py [-h] [-v] Min Max

    Sequ

    positional arguments:
      Min            Minimum
      Max            Maximum

    optional arguments:
      -h, --help     show this help message and exit
      -v, --version  show program's version number and exit
    """
    return range(int(float(args.min)), int(float(args.max)) + 1)


def create_parser():
    parser = argparse.ArgumentParser(
        description='Sequ',
        prog='SEQU'
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s cl3'
    )
    parser.add_argument(
        "min",
        type=int,
        help="minimum"
    )

    parser.add_argument(
        "max",
        type=int,
        help="maximum"
    )
    return parser


def main():
    parser = create_parser()
    parser.set_defaults(func=sequ)
    args = parser.parse_args()
    for i in args.func(sequ):
        print(i)


if __name__ == '__main__':
    main()