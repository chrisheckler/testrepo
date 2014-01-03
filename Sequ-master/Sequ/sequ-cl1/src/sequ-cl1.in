#!/usr/bin/env python
#Copyright © 2013 James Beedy
import sys
sys.path.insert(1, '@pythondir@')
from argparse import ArgumentParser
from sequ.sequ import Sequ as sequ


def create_parser():
    parser = ArgumentParser(
        description='Sequ cl1',
        prog='sequ-cl1'
    )
    parser.add_argument(
        "minimum",
        metavar='minimum',
        help="minimum",
        nargs="?"
    )
    parser.add_argument(
        "maximum",
        metavar='maximum',
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


def main():
    parser = create_parser()

    parser.set_defaults(func=sequ)
    args = parser.parse_args()

    if args.format:
        for i in args.func(args.minimum, args.maximum).sequ_ret():
            print(float(i))
    elif args.equalwidth:
        for i in args.func(args.minimum, args.maximum).sequ_ret():
            print(str(i).zfill(len(str(int(float(args.max))))))
    elif args.increment:
        for i in args.func(args.minimum, args.maximum).sequ_ret():
            print(i)
    elif args.separator:
        if " \ " not in args.separator:
            s = ""
            for i in args.func(args.minimum, args.maximum).sequ_ret():
                if i < int(args.maximum):
                    s += str(i) + args.separator
            s += str(i)
            print(s)
    elif args.equalwidth:
        for i in args.func(args.minimum, args.maximum).sequ_ret():
            print(str(i).zfill(len(str(int(float(args.maximum))))))
    else:
        for i in args.func(args.minimum, args.maximum).sequ_ret():
            print(i)


if __name__ == '__main__':
    main()
