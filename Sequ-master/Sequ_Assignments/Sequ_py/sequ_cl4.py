#!/usr/bin/env python


import sys
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
        "-ff",
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
    parser.add_argument(
        "-f",
        "--file",
        dest="filename",
        help="write report to FILE",
        metavar="FILE"
    )
    parser.add_argument(
        "-n",
        "--number-lines",
        dest="n",
        type=int,
        help="how many lines get printed"
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_false", dest="verbose",
        default=True,
        help="don't print status messages to stdout"
    )
    parser.add_argument(
        '-l',
        '--log',
        default=sys.stdout,
        dest='log',
        type=argparse.FileType('w'),
        help='the file where the sum should be written'
    )
    return parser


def sequ(args):
    if not args.min:
        args.min = 1

    if not args.n:
        if not args.increment:
            return range(int(float(args.min)), int(float(args.max)) + 1, 1)
        else:
            return range(int(float(args.min)), int(float(args.max)) + 1, int(float(args.increment)))
    else:
        if not args.increment:
            return range(int(float(args.min)), int(float(args.min)) + args.n, 1)
        else:
            return range(int(float(args.min)), int(float(args.min)) + args.n, int(float(args.increment)))


def alpha_low_sequ(args):
    if not args.min:
        args.min = "a"

    if not args.n:
        if not args.increment:
            return range(int(alpha_low_to_int(args.min)), int(alpha_low_to_int(args.max)) + 1, 1)
        else:
            return range(int(alpha_low_to_int(args.min)), int(alpha_low_to_int(args.max)) + 1,
                         alpha_low_to_int(args.increment))
    else:
        if not args.increment:
            return range(int(alpha_low_to_int(args.min)), int(alpha_low_to_int(args.min)) + args.n, 1)
        else:
            return range(int(alpha_low_to_int(args.min)), int(alpha_low_to_int(args.min)) + args.n,
                         alpha_low_to_int(args.increment))


def alpha_upper_sequ(args):
    if not args.min:
        args.min = "A"

    if not args.n:
        if not args.increment:
            return range(int(alpha_upper_to_int(args.min)), int(alpha_upper_to_int(args.max)) + 1, 1)
        else:
            return range(int(alpha_upper_to_int(args.min)), int(alpha_upper_to_int(args.max)) + 1,
                         alpha_upper_to_int(args.increment))
    else:
        if not args.increment:
            return range(int(alpha_upper_to_int(args.min)), int(alpha_upper_to_int(args.min)) + args.n, 1)
        else:
            return range(int(alpha_upper_to_int(args.min)), int(alpha_upper_to_int(args.min)) + args.n,
                         alpha_upper_to_int(args.increment))


def roman_low_sequ(args):
    if not args.min:
        args.min = "i"

    if not args.n:
        if not args.increment:
            return range(int(roman_low_to_int(args.min)), int(roman_low_to_int(args.max)) + 1, 1)
        else:
            return range(int(roman_low_to_int(args.min)), int(roman_low_to_int(args.max)) + 1,
                         roman_low_to_int(args.increment))
    else:
        if not args.increment:
            return range(int(roman_low_to_int(args.min)), int(roman_low_to_int(args.min)) + args.n, 1)
        else:
            return range(int(roman_low_to_int(args.min)), int(roman_low_to_int(args.min)) + args.n,
                         roman_low_to_int(args.increment))


def roman_upper_sequ(args):

    if not args.min:
        args.min = "I"

    if not args.n:
        if not args.increment:
            return range(int(roman_upper_to_int(args.min)), int(roman_upper_to_int(args.max)) + 1, 1)
        else:
            return range(int(roman_upper_to_int(args.min)), int(roman_upper_to_int(args.max)) + 1,
                         roman_upper_to_int(args.increment))
    else:
        if not args.increment:
            return range(int(roman_upper_to_int(args.min)), int(roman_upper_to_int(args.min)) + args.n, 1)
        else:
            return range(int(roman_upper_to_int(args.min)), int(roman_upper_to_int(args.min)) + args.n,
                         roman_upper_to_int(args.increment))


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


def file_io(args):
    if args.filename:
        f = open(args.filename, 'r')
        if args.formatwords:
            if args.formatwords == "arabic":
                for i in args.func(args):
                    if args.separator:
                        args.log.write(str(i) + args.separator + f.readline())
                    else:
                        args.log.write(str(i) + " " + f.readline())
                args.log.close()

            elif args.formatwords == "floating":
                for i in args.func(args):
                    if args.separator:
                        args.log.write(str(float(i)) + args.separator + f.readline())
                    else:
                        args.log.write(str(float(i)) + " " + f.readline())
                args.log.close()

            elif args.formatwords == "alpha":
                for i in alpha_low_sequ(args):
                    if args.separator:
                        args.log.write(str(int_to_alpha_low(i)) + args.separator + f.readline())
                    else:
                        args.log.write(str(int_to_alpha_low(i)) + " " + f.readline())
                args.log_close()

            elif args.formatwords == "ALPHA":
                for i in alpha_upper_sequ(args):
                    if args.separator:
                        args.log.write(str(int_to_alpha_upper(i)) + args.separator + f.readline())
                    else:
                        args.log.write(str(int_to_alpha_upper(i)) + " " + f.readline())
                args.log.close()

            elif args.formatwords == "roman":
                for i in roman_low_sequ(args):
                    if args.separator:
                        args.log.write(str(int_to_roman_low(i)) + args.separator + f.readline())
                    else:
                        args.log.write(str(int_to_roman_low(i)) + " " + f.readline())
                args.log.close()

            elif args.formatwords == "ROMAN":
                for i in roman_upper_sequ(args):
                    if args.separator:
                        args.log.write(str(int_to_roman_upper(i)) + args.separator + f.readline())
                    else:
                        args.log.write(str(int_to_roman_upper(i)) + " " + f.readline())
                args.log.close()

            else:
                if type(args.Max) == int:
                    for i in args.func(args):
                        if args.separator:
                            args.log.write(str(i) + args.separator + f.readline())
                        else:
                            args.log.write(str(i) + " " + f.readline())
                    args.log.close()

                elif type(args.Max) == float:
                    for i in args.func(args):
                        if args.separator:
                            args.log.write(str(float(i)) + args.separator + f.readline())
                        else:
                            args.log.write(str(float(i)) + " " + f.readline())
                    args.log.close()

                else:
                    for i in args.func(args):
                        if args.separator:
                            args.log.write(str(i) + args.separator + f.readline())
                        else:
                            args.log.write(str(i) + " " + f.readline())
                    args.log.close()


    elif args.format:
        for i in args.func(args):
            if not i == '\n':
                print(float(i))

    elif args.incrementor:
        for i in args.func(args):
            if i % int(args.incrementor) == 0:
                print(i)

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
            print(str(i).zfill(len(str(int(float(args.max))))))

    elif args.separator:
        s = ""
        for i in args.func(args):
            if " \ " not in args.separator:
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
    file_io(args)

if __name__ == '__main__':
    main()

