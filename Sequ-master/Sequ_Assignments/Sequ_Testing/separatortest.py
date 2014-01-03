#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#Copyright © 2013 James Beedy
#sequ - separator testing

import argparse
import functools


def sequ(args):
    if not args.min:
        args.min = 1
    if not args.increment:
        return range(int(float(args.min)), int(float(args.max)) + 1)
    else:
        return range(int(float(args.min)), int(float(args.max)) + 1, int(float(args.increment)))

#changed implementation of separator: old implementation was very inefficient
#'''''''''''''''''' old implementation''''''''''''''''''''''''''''''''''
#
#if " \ " not in args.separator:
#           print(functools.reduce(lambda x, y: x + args.separator + y,
#                                   map(str, args.func(args))))
#
#'''''''''''''''''' 2nd implementation''''''''''''''''''''''''''''''''''
#
#if " \ " not in args.separator:
#            print(args.separator.join(map(str, args.func(args))))
#
#
#'''''''''''''''''' 3nd implementation''''''''''''''''''''''''''''''''''
#This is by far the fastest implementation of the three.
# Will update following revisions with this implementation of separator
#if " \ " not in args.separator_new_1:
#            s = ""
#            for i in args.func(args):
#                if i < int(args.max):
#                    s += str(i) + args.separator_new_1
#            s += str(i)
#            print(s)





def main():

    parser = create_parser()
    parser.set_defaults(func=sequ)
    args = parser.parse_args()

    if args.increment:
        for i in args.func(args):
            print(i)

    elif args.separator_old:
        if " \ " not in args.separator_old:
            print(args.separator_old.join(map(str, args.func(args))))

    elif args.separator_new:
        if " \ " not in args.separator_new:
            print(functools.reduce(lambda x, y: x + args.separator_new + y,
                                   map(str, args.func(args))))

    elif args.separator_new_1:
        if " \ " not in args.separator_new_1:
            s = ""
            for i in args.func(args):
                if i < int(args.max):
                    s += str(i) + args.separator_new_1
            s += str(i)
            print(s)

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
    parser.add_argument(
        '-so',
        '--separator-old',
        dest='separator_old',
        help='use the STRING to separate numbers',
        nargs="?"
    )
    parser.add_argument(
        '-sn',
        '--separator-new',
        dest='separator_new',
        help='use the STRING to separate numbers',
        nargs="?"
    )
    parser.add_argument(
        '-sn1',
        '--separator-new-1',
        dest='separator_new_1',
        help='use the STRING to separate numbers',
        nargs="?"
    )

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s cl3'
    )
    parser.add_argument(
        '-i',
        '--increment',
        help='incrimental regulator',
        nargs="?"
    )
    return parser

if __name__ == '__main__':
    main()