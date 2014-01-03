#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import re

class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass
class InvalidRomanNumeralError(ValueError): pass

roman_numeral_map = (('m',  1000),
                     ('cm', 900),
                     ('d',  500),
                     ('cd', 400),
                     ('c',  100),
                     ('xc', 90),
                     ('l',  50),
                     ('xl', 40),
                     ('x',  10),
                     ('ix', 9),
                     ('v',  5),
                     ('iv', 4),
                     ('i',  1))

roman_numeral_pattern_low = re.compile("""
    ^                   # beginning of string
    m{0,4}              # thousands - 0 to 4 m's
    (cm|cd|d?c{0,3})    # hundreds - 900 (cm), 400 (cd), 0-300 (0 to 3 c's),
                        #            or 500-800 (d, followed by 0 to 3 c's)
    (xc|xl|l?x{0,3})    # tens - 90 (xc), 40 (xl), 0-30 (0 to 3 x's),
                        #        or 50-80 (l, followed by 0 to 3 x's)
    (ix|iv|v?i{0,3})    # ones - 9 (ix), 4 (iv), 0-3 (0 to 3 i's),
                        #        or 5-8 (v, followed by 0 to 3 i's)
    $                   # end of string
    """, re.VERBOSE)

def to_roman(n):
    """convert integer to Roman numeral"""
    if not isinstance(n, int):
        raise NotIntegerError('non-integers can not be converted')
    if not (0 < n < 5000):
        raise OutOfRangeError('number out of range (must be 1..4999)')
    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result

def from_roman(s):
    """convert Roman numeral to integer"""
    if not isinstance(s, str):
        raise InvalidRomanNumeralError('input must be a string')
    if not s:
        raise InvalidRomanNumeralError('input can not be blank')
    if not roman_numeral_pattern_low.search(s):
        raise InvalidRomanNumeralError('invalid Roman numeral: {0}'.format(s))
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index : index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result

