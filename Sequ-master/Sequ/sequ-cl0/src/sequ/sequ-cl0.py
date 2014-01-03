#!/usr/bin/env python
#Copyright © 2013 James Beedy
import sys
sys.path.insert(1, '@pythondir@')
from argparse import ArgumentParser
from sequ.sequ import Sequ as sequ

def create_parser():
    parser = ArgumentParser(
        description='Sequ-cl0',
        prog='sequ-cl0'
    )
    parser.add_argument(
        'minimum',
        metavar='minimum',
        help="minimum",
        type=int
    )
    parser.add_argument(
        'maximum',
        metavar='maximum',
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

def main():
    parser = create_parser()
    parser.set_defaults(func=sequ)
    args = parser.parse_args()

    for i in args.func(args.minimum, args.maximum).sequ_ret():
        print(i)


if __name__ == '__main__':
    main()


