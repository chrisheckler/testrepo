#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#Copyright © 2013 James Beedy

# Removed increment argument. Replaced with incrementer.
#
import sys
import re
sys.path.insert(1, '/usr/local/lib/python2.7/dist-packages')
import argparse
import sequ.seqmapio as seqmap
from sequ.romanl import to_roman as to_romanl
from sequ.romanl import from_roman as from_romanl
from sequ.romanl import roman_numeral_pattern_low as rom_pat_low
from sequ.romanu import to_roman as to_romanu
from sequ.romanu import from_roman as from_romanu
from sequ.romanu import roman_numeral_pattern_upper as rom_pat_up


def create_parser():
    parser = argparse.ArgumentParser(
        description='Sequ cl3',
        prog='sequ-cl3'
    )
    parser.add_argument(
        'minimum',
        metavar='minimum',
        help='minimum',
        nargs='?'
    )
    parser.add_argument(
        'maximum',
        metavar='maximum',
        help='maximum'
    )
    parser.add_argument(
        'incrementer',
        metavar='incrementer',
        help = 'incrementer',
        nargs='?'
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-s',
        '--separator',
        help='use the STRING to separate numbers',
        nargs="?",
        type= str
    )
    group.add_argument(
        '-e',
        '--equal-width',
        help='pad 0s to each element in the list < len(max)',
        dest='equalwidth',
        const=True,
        action='store_const'
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s cl2'
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
    parser.add_argument(
        '-F',
        '--formatwords',
        choices=['arabic',
                 'floating',
                 'alpha',
                 'ALPHA',
                 'roman',
                 'ROMAN'],
        help='use typesetting',
        nargs="?"
    )
    return parser


def parsefunc(args):
    seqlst = []
    seq = seqmap.SequFuncs(args)
    low_re = re.compile("([a-z])")
    high_re = re.compile("([A-Z])")

    if args.formatwords:
        if args.formatwords == "arabic":
            for i in seq.sequ_ret():
                seqlst.append(i)
        elif args.formatwords == "floating":
            for i in seq.sequ_ret():
                seqlst.append(float(i))
        elif args.formatwords == "alpha":
            for i in seq.alpha_low_sequ():
                if (0 < int(args.minimum) < 27) and (1 < int(args.maximum) < 27):
                    for i in seq.alpha_low_sequ():
                        seqlst.append(chr(int(i + 96)))
                else:
                    print('Please use correct range for alpha (1 - 26)')
        elif args.formatwords == "ALPHA":
                if (0 < int(args.minimum) < 27) and (1 < int(args.maximum) < 27):
                    for i in seq.alpha_low_sequ():
                        seqlst.append(chr(int(i) + 64))
                else:
                    print('Please use correct range for alpha (1 - 26)')
        elif args.formatwords == "roman":
            for i in seq.roman_low_sequ():
                seqlst.append(to_romanl(i))
        elif args.formatwords == "ROMAN":
            for i in seq.roman_upper_sequ():
                seqlst.append(to_romanu(i))
        else:
            if type(args.maximum) == int:
                for i in seq.sequ_ret():
                    seqlst.append(i)
            elif type(args.maximum) == float:
                for i in seq.sequ_ret():
                    seqlst.append(float(i))
            elif type(args.maximum) == str:
                if rom_pat_up.search(args.maximum):
                    for i in seq.roman_upper_sequ():
                        seqlst.append(i)
                elif rom_pat_low.search(args.maximum):
                    for i in seq.roman_low_sequ():
                        seqlst.append(i)
                elif high_re.search(args.maximum):
                    for i in seq.alpha_high_sequ():
                        seqlst.append(i)
                elif low_re.search(args.maximum):
                    for i in seq.alpha_low_sequ():
                        seqlst.append(i)
                else:
                    for i in seq.sequ_ret():
                         seqlst.append(i)
    else:
        for i in seq.sequ_ret():
            seqlst.append(i)
    return seqlst


def main():
    parser = create_parser()
    args = parser.parse_args()
    p = parsefunc(args)
    if args.format:
        for i in p:
            print(float(i))
    elif args.separator:
        if " \'" not in args.separator:
            print(args.separator.join(map(str, p)))
    elif args.equalwidth:
        for i in p:
            print(str(i).zfill(len(str(int(float(args.maximum))))))
    elif args.pad:
        if "\'" not in args.pad:
            j = 0
            for i in map(str, p):
                if len(i) >= j:
                    j = len(i)
            k = 0
            for i in map(str, p):
                if len(i) <= j:
                    k = j - len(i)
                    while len(i) < j:
                        i = k*str(args.pad) + str(i)
                    print(i)
                else:
                    print("Pad character length must be less than 2! ")
        else:
            print("String must not contain the backslash! ")
    elif args.padspaces:
        j = 0
        for i in map(str, p):
            if len(i) >= j:
                j = len(i)
        k = 0
        for i in map(str, p):
            if len(i) < j:
                k = j - len(i)
                while len(i) < j:
                    i = k*" " + str(i)
            print(i)
    elif args.words:
        print(" ".join(map(str, p)))
    else:
        for i in p:
            print(i)

if __name__ == '__main__':
    main()
