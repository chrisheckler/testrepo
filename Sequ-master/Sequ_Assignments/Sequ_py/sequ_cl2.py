#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#Copyright © 2013 James Beedy
#CS300 Assignment 4: cl2

import argparse
import functools
#Added support for float type input for increment and for Min and Max values.
#TODO: Fix pad to accomodate larger than 1 character pads
#TODO: Fix Increment and Min optional values to work for all options
# Adding coverage.txt support
# Adding support for integrated testing
# Rearranged and correcting some formatting


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
                    s += str(i) + args.separator
            s += str(i)
            print(s)
    elif args.pad:
        if " \ " not in args.pad:
            if len(args.pad) < 2:
                for i in map(str, args.func(args)):
                    if not i == '\n':
                        len(i) < len(args.max)
                        while len(i) < len(args.max):
                            i = args.pad + str(i)
                        print(i)
            else:
                print("Pad character length must be less than 2! ")
        else:
            print("String must not contain the backslash! ")

    elif args.padspaces:
        for i in map(str, args.func(args)):
            if len(i) < len(args.max):
                while len(i) < len(args.max):
                    i = " " + str(i)
            print(i)

    elif args.equalwidth:
        for i in args.func(args):
            print(str(i).zfill(len(str(int(float(args.Max))))))

    elif args.words:
        print(" ".join(map(str, args.func(args))))

    else:
        for i in args.func(args):
            print(i)


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
    parser.add_argument(
        '-p',
        '--pad',
        metavar='PAD',
        help='pad string to create equal-width elements',
        type=str,
        const=True,
        nargs="?"
    )
    parser.add_argument(
        "-P",
        '--padspaces',
        help='pad string with ' ' to create equal-width elements',
        dest='padspaces',
        const=True,
        action='store_const'
    )
    parser.add_argument(
        '-w',
        '--words',
        help='outputs a single space separated string',
        dest='words',
        const=True,
        action='store_const'
    )
    return parser

if __name__ == '__main__':
    main()