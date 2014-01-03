#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#Copyright © 2013 James Beedy
#seau_cl3:

import argparse
import functools

#TODO: Fix pad to accomodate larger than 1 character pads
#TODO: Fix Increment and min optional values to work for all options
#created character mappings for alpha and roman conversions
#Updated separator to rev. 3


def create_parser():
    parser = argparse.ArgumentParser(
        description='Sequ',
        prog='SEQU'
    )
    parser.add_argument(
        "min",
        metavar='min',
        help="minimum",
        nargs='?'
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
        metavar='STRING',
        help='use the STRING to separate numbers',
        dest='separator',
        type=str
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
        dest='incrementor',
        type=str,
        help='incremental regulator'
    )
    parser.add_argument(
        'increment',
        metavar='INC',
        help='incremental regulator',
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
    parser.add_argument(
        '-F',
        '--formatwords',
        choices=['arabic',
                'floating',
                 'alpha',
                 'ALPHA',
                 'roman',
                 'ROMAN'],
        help='use typesetting'
    )
    return parser


def sequ(args):
    if not args.min:
        args.min = 1

    if not args.increment:
        return range(int(float(args.min)), int(float(args.max)) + 1, 1)
    else:
        return range(int(float(args.min)), int(float(args.max)) + 1, int(float(args.increment)))


def alpha_low_sequ(args):
    if not args.min:
        args.min = "a"

    if not args.increment:
        return range(int(alpha_low_to_int(args.min)), int(alpha_low_to_int(args.max)) + 1, 1)
    else:
        return range(int(alpha_low_to_int(args.min)), int(alpha_low_to_int(args.max)) + 1,
                     int(args.increment))


def alpha_upper_sequ(args):
    if not args.min:
        args.min = "A"

    if not args.increment:
        return range(int(alpha_upper_to_int(args.min)), int(alpha_upper_to_int(args.max)) + 1, 1)
    else:
        return range(int(alpha_upper_to_int(args.min)), int(alpha_upper_to_int(args.max)) + 1,
                     int(args.increment))


def roman_low_sequ(args):
    if not args.min:
        args.min = "i"

    if not args.increment:
        return range(int(roman_low_to_int(args.min)), int(roman_low_to_int(args.max)) + 1, 1)
    else:
        return range(int(roman_low_to_int(args.min)), int(roman_low_to_int(args.max)) + 1,
                     int(roman_low_to_int(args.increment)))


def roman_upper_sequ(args):
    if not args.min:
        args.min = "I"

    if not args.increment:
        return range(int(roman_upper_to_int(args.min)), int(roman_upper_to_int(args.max)) + 1, 1)
    else:
        return range(int(roman_upper_to_int(args.min)), int(roman_upper_to_int(args.max)) + 1,
                     int(roman_upper_to_int(args.increment)))


alpha_map_low = tuple(zip(
    (26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1),
    ("z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d",
     "c", "b", "a")))


def int_to_alpha_low(input_int):
    result = []
    for integer, alpha in alpha_map_low:
        count = input_int // integer
        result.append(alpha * count)
        input_int -= integer * count
    return ''.join(result)


def alpha_low_to_int(input_alpha):
    i = result = 0
    for integer, alpha in alpha_map_low:
        while input_alpha[i:i + len(alpha)] == alpha:
            result += integer
            i += len(alpha)
    return result


alpha_map_caps = tuple(zip(
    (26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1),
    ("Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "N", "M", "L", "K", "J", "I", "H", "G", "F", "E", "D",
     "C", "B", "A")))


def int_to_alpha_upper(input_int):
    result = []
    for integer, alpha in alpha_map_caps:
        count = input_int // integer
        result.append(alpha * count)
        input_int -= integer * count
    return ''.join(result)


def alpha_upper_to_int(input_alpha):
    i = result = 0
    for integer, alpha in alpha_map_caps:
        while input_alpha[i:i + len(alpha)] == alpha:
            result += integer
            i += len(alpha)
    return result


numeral_map_low = tuple(zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i')
))


def int_to_roman_low(input_int):
    result = []
    for integer, numeral in numeral_map_low:
        count = input_int // integer
        result.append(numeral * count)
        input_int -= integer * count
    return ''.join(result)


def roman_low_to_int(input_rom):
    i = result = 0
    for integer, numeral in numeral_map_low:
        while input_rom[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result


numeral_map_upper = tuple(zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
))


def int_to_roman_upper(input_int):
    result = []
    for integer, numeral in numeral_map_upper:
        count = input_int // integer
        result.append(numeral * count)
        input_int -= integer * count
    return ''.join(result)


def roman_upper_to_int(input_rom):
    i = result = 0
    for integer, numeral in numeral_map_upper:
        while input_rom[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result


def parsing(args):
            if args.format:
                for i in args.func(args):
                    if not i == '\n':
                        print(float(i))

            elif args.incrementor:
                for i in args.func(args):
                    if i % int(args.incrementor) == 0:
                        print(i)

            elif args.pad:
                for i in map(str, args.func(args)):
                    if not i == '\n':
                        len(i) < len(args.max)
                        while len(i) < len(args.max):
                            i = args.pad + str(i)
                            print(i)
                print(args.pad + str(i))

            elif args.padspaces:
                for i in map(str, args.func(args)):
                    if len(i) < len(args.max):
                        while len(i) < len(args.max):
                            i = " " + str(i)
                    print(i)

            elif args.equalwidth:
                for i in args.func(args):
                    print(str(i).zfill(len(str(int(float(args.max))))))

            elif args.separator:
                if " \ " not in args.separator:
                    s = ""
                for i in args.func(args):
                    if i < int(args.max):
                        s += str(i) + args.separator
                s += str(i)
                print(s)

            elif args.words:
                print(" ".join(map(str, args.func(args))))

            elif args.formatwords:
                if args.formatwords == "arabic":
                        for i in args.func(args):
                            print(i)

                elif args.formatwords == "floating":
                    for i in args.func(args):
                        print(float(i))

                elif args.formatwords == "alpha":
                    for i in alpha_low_sequ(args):
                        print(int_to_alpha_low(i))

                elif args.formatwords == "ALPHA":
                    for i in alpha_upper_sequ(args):
                        print(int_to_alpha_upper(i))

                elif args.formatwords == "roman":
                    for i in roman_low_sequ(args):
                        print(int_to_roman_low(i))

                elif args.formatwords == "ROMAN":
                    for i in roman_upper_sequ(args):
                        print(int_to_roman_upper(i))
                else:
                    if type(args.max) == int:
                        for i in args.func(args):
                            print(i)
                    if type(args.max) == float:
                        for i in args.func(args):
                            print(float(i))
                    if type(args.max) == str:
                        for i in args.func(args):
                            print(float(i))

            else:
                for i in args.func(args):
                    print(i)


def main():
    parser = create_parser()
    parser.set_defaults(func=sequ)
    args = parser.parse_args()
    parsing(args)

if __name__ == '__main__':
    main()

