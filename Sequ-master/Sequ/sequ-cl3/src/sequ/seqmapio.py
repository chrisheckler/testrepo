#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Copyright © 2013 James Beedy

import sys
sys.path.insert(1, '/usr/local/lib/python2.7/dist-packages')
import re
from sequ.romanl import to_roman as to_romanl
from sequ.romanl import from_roman as from_romanl
from sequ.romanl import roman_numeral_pattern_low as rom_pat_low
from sequ.romanu import roman_numeral_pattern_upper as rom_pat_up
from sequ.romanu import from_roman as from_romanu
from sequ.romanu import to_roman as to_romanu

#TODO: Format control!!*!*!*! -> done
#TODO: Object orient code -> 2/3 done
#TODO: Fix pad to accomodate larger than 1 character pads
#TODO: Fix Increment and minimum optional values to work for all options -> Fixed
#TODO: create character mappings for alpha and roman conversions -> Done

class SequFuncs(object):
    def __init__(self, args):
        # Define pattern to detect valid Roman numerals
        self.roman_numeral_pattern_upper = rom_pat_up
        self.roman_numeral_pattern_low = rom_pat_low
        self.maximum = args.maximum

        if not args.minimum:
            if self.roman_numeral_pattern_upper.search(self.maximum):
                self.minimum = "I"
            elif self.roman_numeral_pattern_low.search(args.maximum):
                self.minimum = 'i'
            else:
                self.minimum = 1
        else:
            self.minimum = args.minimum

        if not args.incrementer:
            if self.roman_numeral_pattern_upper.search(self.maximum):
                self.incrementer = "I"
            elif self.roman_numeral_pattern_low.search(args.maximum):
                self.incrementer = 'i'
            else:
                self.incrementer = 1
        else:
            self.incrementer = args.incrementer

    def sequ_ret(self):
        return range(
            int(self.minimum),
            int(self.maximum) + 1,
            int(self.incrementer)
        )

    def alpha_low_sequ(self):
        return range(int(self.minimum),
                     int(self.maximum) + 1,
                     int(self.incrementer)
        )

    def alpha_upper_sequ(self):
        return range(int(self.minimum),
                     int(self.maximum) + 1,
                     int(self.incrementer)
        )

    def roman_low_sequ(self):
        return range(
            int(from_romanl(str(self.minimum))),
            int(from_romanl(str(self.maximum))) + 1,
            int(from_romanl(str(self.incrementer)))
        )

    def roman_upper_sequ(self):
        return range(
            int(from_romanu(str(self.minimum))),
            int(from_romanu(str(self.maximum))) + 1,
            int(from_romanu(str(self.incrementer)))
        )
