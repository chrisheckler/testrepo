#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import doctest
import docutils
import romanl
import unittest 
from romanl import to_roman
from romanl import from_roman
from romanl import NotIntegerError
import unittest

class Knownvalues(unittest.TestCase):
    known_values = ( (1, 'i'),
                     (2, 'ii'),
                     (3, 'iii'),
                     (4, 'iv'),
                     (5, 'v'),
                     (6, 'vi'),
                     (7, 'vii'),
                     (8, 'viii'),
                     (9, 'ix'),
                     (10, 'x'),
                     (50, 'l'),
                     (100, 'c'),
                     (500, 'd'),
                     (1000, 'm'),
                     (31, 'xxxi'),
                     (148, 'cxlviii'),
                     (294, 'ccxciv'),
                     (312, 'cccxii'),
                     (421, 'cdxxi'),
                     (528, 'dxxviii'),
                     (621, 'dcxxi'),
                     (782, 'dcclxxxii'),
                     (870, 'dccclxx'),
                     (941, 'cmxli'),
                     (1043, 'mxliii'),
                     (1110, 'mcx'),
                     (1226, 'mccxxvi'),
                     (1301, 'mccci'),
                     (1485, 'mcdlxxxv'),
                     (1509, 'mdix'),
                     (1607, 'mdcvii'),
                     (1754, 'mdccliv'),
                     (1832, 'mdcccxxxii'),
                     (1993, 'mcmxciii'),
                     (2074, 'mmlxxiv'),
                     (2152, 'mmclii'),
                     (2212, 'mmccxii'),
                     (2343, 'mmcccxliii'),
                     (2499, 'mmcdxcix'),
                     (2574, 'mmdlxxiv'),
                     (2646, 'mmdcxlvi'),
                     (2723, 'mmdccxxiii'),
                     (2892, 'mmdcccxcii'),
                     (2975, 'mmcmlxxv'),
                     (3051, 'mmmli'),
                     (3185, 'mmmclxxxv'),
                     (3250, 'mmmccl'),
                     (3313, 'mmmcccxiii'),
                     (3408, 'mmmcdviii'),
                     (3501, 'mmmdi'),
                     (3610, 'mmmdcx'),
                     (3743, 'mmmdccxliii'),
                     (3844, 'mmmdcccxliv'),
                     (3888, 'mmmdccclxxxviii'),
                     (3940, 'mmmcmxl'),
                     (3999, 'mmmcmxcix'),
                     (4000, 'mmmm'),
                     (4500, 'mmmmd'),
                     (4888, 'mmmmdccclxxxviii'),
                     (4999, 'mmmmcmxcix'))


    def test_to_roman_known_values(self):
        '''to_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = to_roman(integer)
            self.assertEqual(numeral, result)

    def test_from_roman_known_values(self):
        '''from_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = from_roman(numeral)
            self.assertEqual(integer, result)



class FromRomanBadinput(unittest.TestCase):

    # modified to accommodate new values -> 5000
    # to ensure that the from_roman() function should fail when you pass
    # it a string with too many repeated numerals
    def test_too_many_repeated_numerals(self):
        """from_roman should fail with too many repeated numerals"""
        for s in ('mmmmm', 'dd', 'cccc', 'll', 'xxxx', 'vv', 'iiii'):
            self.assertRaises(romanl.InvalidRomanNumeralError, from_roman, s)

    # test certain patterns aren’t repeated. For example, ix is 9, but ixix is never valid
    def test_repeated_pairs(self):
        """from_roman should fail with repeated pairs of numerals"""
        for s in ('cmcm', 'cdcd', 'xcxc', 'xlxl', 'ixix', 'iviv'):
            self.assertRaises(romanl.InvalidRomanNumeralError, from_roman, s)

    # test numerals appear in the correct order, from highest to lowest value
    def test_malformed_antecedents(self):
        """from_roman should fail with malformed antecedents"""
        for s in ('iimxcc', 'vx', 'dcm', 'cmm', 'ixiv',
                  'mcmc', 'xcx', 'ivi', 'lm', 'ld', 'lc'):
            self.assertRaises(romanl.InvalidRomanNumeralError, from_roman, s)

    # test for the empty string
    def testBlank(self):
        """from_roman should fail with blank string"""
        self.assertRaises(romanl.InvalidRomanNumeralError, from_roman, '')

class ToRomanBadInput(unittest.TestCase):
    # raised numeral input value. Previous: 4000

    def test_too_large(self):
        """to_roman should fail with large input"""
        self.assertRaises(romanl.OutOfRangeError, to_roman, 5000)

    def test_zero(self):
        """to_roman should fail with 0 input"""
        self.assertRaises(romanl.OutOfRangeError, to_roman, 0)

    def test_negative(self):
        """to_roman should fail with negative input"""
        self.assertRaises(romanl.OutOfRangeError, to_roman, -1)

    def test_non_integer(self):
        """to_roman should fail with non-integer input"""
        self.assertRaises(romanl.NotIntegerError, to_roman, 0.5)


class Roundtripcheck(unittest.TestCase):
    def test_roundtrip(self):
        """from_roman(to_roman(n))==n for all n"""
        for integer in range(1, 5000):
            numeral = to_roman(integer)
            result = from_roman(numeral)
            self.assertEqual(integer, result)


    def test_to_roman_returns_x_for_10(self):
        self.assertEqual('x', to_roman(10))


class TestNotintegerError(unittest.TestCase):
    def test_(self):
        not_integer_error = NotIntegerError()

class TestToRoman(unittest.TestCase):
    def test_to_roman_raises_not_integer_error_for_(self):
        self.assertRaises(NotIntegerError, lambda: to_roman('#'))

    def test_to_roman_returns_x_for_10(self):
        self.assertEqual('x', to_roman(10))



class TestFromRoman(unittest.TestCase):
    def test_from_roman(self):
        # self.assertEqual(expected, from_roman(s))
        assert False # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
