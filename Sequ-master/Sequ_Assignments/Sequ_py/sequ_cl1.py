#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#Copyright © 2013 James Beedy
#sequ_cl1
#updated separator

import argparse
import functools

#Added extra feature not in spec: Ability to input int or float for min, max or inc
#Will carry float or int input feature into future revisions

#Create ArgumentParser


def create_parser():
    parser = argparse.ArgumentParser(
        description='Sequ',
        prog='SEQU'
    )
    parser.add_argument(
        "min",
        metavar='min',
        help="minimum",
        nargs="?"
    )
    parser.add_argument(
        "max",
        metavar='max',
        help="maximum"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-s',
        '--separator',
        help='use the STRING to separate numbers',
        nargs="?"
    )
    group.add_argument(
        '-e',
        '--equal-width',
        help='pad 0s to each element in the list',
        dest='equalwidth',
        const=True,
        action='store_const'
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s cl3'
    )
    parser.add_argument(
        "-f",
        '--format',
        help='format to floating-point',
        dest='format',
        const=True,
        action='store_const'
    )
    parser.add_argument(
        '-i',
        '--increment',
        help='incrimental regulator',
        nargs="?"
    )
    return parser


def sequ(args):
    if not args.min:
        args.min = 1
    if not args.increment:
        return range(int(float(args.min)), int(float(args.max)) + 1)
    else:
        return range(int(float(args.min)), int(float(args.max)) + 1, int(float(args.increment)))


def main():

    parser = create_parser()
    parser.set_defaults(func=sequ)
    args = parser.parse_args()
    if args.format:
        for i in args.func(args):
            print(float(i))
    elif args.equalwidth:
        for i in args.func(args):
            print(str(i).zfill(len(str(int(float(args.max))))))
    elif args.increment:
        for i in args.func(args):
            print(i)
    elif args.separator:
        if " \ " not in args.separator:
            s = ""
            for i in args.func(args):
                if i < int(args.max):
                    s += str(i) + args.separator_new_1
            s += str(i)
            print(s)
    elif args.equalwidth:
        for i in args.func(args):
            print(str(i).zfill(len(str(int(float(args.Max))))))
    else:
        for i in args.func(args):
            print(i)


if __name__ == '__main__':
    main()