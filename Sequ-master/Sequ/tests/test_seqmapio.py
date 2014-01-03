import unittestfrom seqmapio import SequFuncs


class TestSequFuncs(unittest.TestCase):
    def test___init__(self):
        # sequ_funcs = SequFuncs(args)
        assert False # TODO: implement your test here

    def test_alpha_low_sequ(self):
        # sequ_funcs = SequFuncs(args)
        # self.assertEqual(expected, sequ_funcs.alpha_low_sequ())
        assert False # TODO: implement your test here

    def test_alpha_upper_sequ(self):
        # sequ_funcs = SequFuncs(args)
        # self.assertEqual(expected, sequ_funcs.alpha_upper_sequ())
        assert False # TODO: implement your test here

    def test_roman_low_sequ(self):
        # sequ_funcs = SequFuncs(args)
        # self.assertEqual(expected, sequ_funcs.roman_low_sequ())
        assert False # TODO: implement your test here

    def test_roman_upper_sequ(self):
        # sequ_funcs = SequFuncs(args)
        # self.assertEqual(expected, sequ_funcs.roman_upper_sequ())
        assert False # TODO: implement your test here

    def test_sequ_ret(self):
        # sequ_funcs = SequFuncs(args)
        # self.assertEqual(expected, sequ_funcs.sequ_ret())
        assert False # TODO: implement your test here

    def test_creation_with_20_raises_attribute_error(self):
        self.assertRaises(AttributeError, lambda: SequFuncs('20'))

    def test_creation_with_1_raises_attribute_error(self):
        self.assertRaises(AttributeError, lambda: SequFuncs(1))

if __name__ == '__main__':
    unittest.main()
