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


class RomanLowRangeError(ValueError):
    pass


class RomanUpRangeError(ValueError):
    pass


class RomanTypeError(ValueError):
    pass


class MaxAndNumError(ValueError):
    pass


class MaxMustBeMaxInputError(ValueError):
    pass


class MinMustBeMinInputError(ValueError):
    pass


class AlphaLowRangeError(ValueError):
    pass


class AlphaUpRangeError(ValueError):
    pass


class IncrementerError(ValueError):
    pass


class NoInputError(ValueError):
    pass


class RangeInputError(ValueError):
    pass


class SequFuncs(object):
    def __init__(self, args):
        # Define compiled patterns for checking 
        #patterns to detect valid Roman numerals
        self.rom_num_pat_up = rom_pat_up
        self.rom_num_pat_low = rom_pat_low
        self.low_re = re.compile("([a-z])")
        self.high_re = re.compile("([A-Z])")
        self.int_map = re.compile("([0-9])")
       
        # Create tmp_vlaues to hole data until 
        #we are ready to assign it permenantly 
        if not args.maximum:
            if not numlines:
                raise NoInputError('Cannot have no input!.')
            else:
                #Creates a new maxval when numlines ius supplied
                self.maximum = args.minimum + args.numlines
                self.incrementer = args.incrementer
                self.minimum = args.minimum
        elif args.maximum > args.minimum: # Check that args.maximum is the maximum 
            self.maximum = args.maximum
            self.incrementer = args.incrementer
            self.minimum = args.minimum
        else:
            raise MaxMustBeMaxInputError('Maximum value must be the maximum value!')
        if self.rom_num_pat_low.search(args.minimum):
            if self.rom_num_pat_low.search(args.incrementer):
                if self.rom_num_pat_low.search(args.maximum):
                    self.minimum = int(from_romanl(args.minimum)) 
                    self.maximum = int(from_romanl(args.maximum))
                    self.incrementer = int(from_romanl(args.incrementer))
            elif type(args.incrementer) == int:
                if int(from_romanl(args.minimum)) + int(from_romanl(args.maximum)) < 4999: # Check that input is in roman range
                    self.minimum = int(from_roman(args.minimum))
                    self.maximum = int(from_romanl(args.maximum))
                    self.incrementer = int(from_romanl(args.incrementer))
                else:
                    raise RomanlowRangeError('Please enter values within the roman range!')
            else:
                raise RomanTypeError('Please enter consistant value types!')
        else:
            args.minimum = 1
            self.minimum = args.minimum 
            self.maximum = args.maximum
            self.incrementer = 1
        
        if self.rom_num_pat_up.search(args.incrementer):
            self.minimum = args.minimum
            self.maximum = int(from_romanu(args.maximum))
            self.incrementer = int(from_romanu(args.incrementer))
             
        elif type(args.incrementer) == int:
            if int(from_romanu(args.minimum)) + int(from_romanu(args.maximum)) < 4999: # Check that input is in roman range
                self.minimum = args.minimum
                self.maximum = int(from_romanu(args.maximum))
                self.incrementer = int(from_romanu(args.incrementer))
            else:
                raise RomanlowRangeError('Please enter values within the roman range!')
        else:
            raise RomanTypeError('Please enter consistant value types!')

        if self.rom_num_pat_up.search(args.maximum):
            args.minimum = 'I'
            if self.rom_num_pat_up.search(args.minimum):
                self.minimum = int(from_romanu(args.minimum)) 
                self.maximum = int(from_romanu(args.maximum))
                self.incrementer = 1
        elif type(args.minimum) == int:
            if args.minimum + int(from_romanu(args.maximum)) < 4999: # Check that input is in roman range
                self.minimum = args.minimum
                self.maximum = int(from_romanu(args.maximum))
                self.incrementer = 1
            else:
                raise RomanlowRangeError('Please enter values within the roman range!')
        else:
            raise RomanTypeError('Please enter consistant value types!')        
        if self.low_re.search(args.minimum):
            if self.low_re.search(args.incrementer):
                if (ord(args.minimum) - 96) + (ord(args.incrementer) - 96) < 27:
                    self.minimum = ord(args.minimum) - 96
                    self.maximum = self.minimum + ord(args.incrementer) - 96
                    self.incrementer = ord(args.incrementer)
                else:
                    raise AlphaLowRangeError('Please enter values within the alpha range!')
            else:
                 args.incrementer = 'a'
                 self.incrementer = ord(args.incrementer)
                 if (ord(args.minimum) - 96 + ord(args.incrementer) - 96) < 27:
                    self.minimum = args.minimum
                    self.maximum = args.minimum + ord(args.incrementer) - 96
                    self.incrementer = args.incrementer
        elif self.low_re.search(args.incrementer):
            if self.low_re.search(args.minimum):
                if (ord(args.minimum) - 96 + ord(tmp_numlines) - 96) < 27:
                    self.minimum = ord(args.minimum) - 96
                    self.maximum = self.minimum + ord(args.incrementer) - 96
                    self.incrementer = ord(args.incrementer)
                else:
                    raise AlphaUpRangeError('Please enter values within the alpha range!')
        
        if self.high_re.search(args.incrementer):
            if type(args.incrementer) == int and args.incrementer <= 26:
                if self.high_re.search(args.minifmum):
                    if (ord(args.minimum) - 64 + ord(args.incrementer) - 64) < 27:
                        self.minimum = ord(args.minimum) - 64
                        self.maximum = self.minimum + ord(args.incrementer) - 64
                        self.incrementer = args.incrementer
                    else:
                        raise AlphaLowRangeError('Please enter values within the alpha range!')
                elif type(args.minimum) == int:
                    if (ord(args.minimum) - 96) + (ord(args.incrementer) - 96) < 27:
                        self.minimum = args.minimum
                        self.maximum = args.minimum + ord(tmp_numlines) - 64
                        self.incrementer = args.incrementer
                    else:
                        if self.high_re.search(args.incrementer):
                            if self.high_re.search(args.minimum):
                                if (ord(args.minimum) - 64 + ord(args.incrementer) - 64) < 27:
                                    self.minimum = ord(args.minimum) - 64
                                    self.maximum = args.minimum + ord(args.incrementer) - 64
                                    self.incrementer = ord(args.incrementer)
                                else:
                                    raise AlphaUpRangeError('Please enter values within the alpha range!')
                            else:
                                raise RomanTypeError('Please enter consistant value types!')
            elif self.int_map.search(args.maximum):
                if self.int_map.search(args.incrementer):
                    if self.int_map.search(args.minimum):
                        if args.minimum < args.maximum:
                            if (args.incrementer * 2) < (args.maximum + args.minimum):
                                self.minimum = args.minimum 
                                self.maximum = args.maximum
                                self.incrementer = args.incrementer
                            else:
                                raise IncrementerError('Please enter min < max!') 
                        else:
                            raise MaxAndMinError('Please enter min < max!')
        elif type(args.minimum) == int:
            self.minimum = args.minimum
            self.maximum = args.maximum
            self.incrementer = args.incrementer
            if self.high_re.search(args.maximum):
                if self.high._re.search(args.minimum):
                    if (ord(args.minimum) - 64 + ord(tmp_numlines) - 64) < 27:
                         self.minimum = ord(args.minimum) - 64
                         self.maximum = ord(args.maximum) - 64
                         self.incrementer = ord(args.incrementer) - 64
                    else:
                        raise AlphaUpRangeError('Please enter values within the alpha range!')


    def sequ_ret(self):
        return range(
            int(self.minimum),
            int(self.maximum) + 1,
            int(self.incrementer)
            )
