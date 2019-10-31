import unittest
import os
import hash_functions


class TestHashFunctions(unittest.TestCase):
    def test_check_hashable_true(self):
        check_true = hash_functions.check_hashable('cat')
        self.assertEqual(check_true, True)

    def test_check_hashable_false(self):
        check_false = hash_functions.check_hashable([])
        self.assertEqual(check_false, False)

    def test_check_integer_true(self):
        check_true = hash_functions.check_integer(3)
        self.assertEqual(check_true, True)

    def test_check_integer_false1(self):
        check_false = hash_functions.check_integer(-1)
        self.assertEqual(check_false, False)

    def test_check_integer_false2(self):
        check_false = hash_functions.check_integer('bad')
        self.assertEqual(check_false, False)

    def test_h_ascii(self):
        mart = hash_functions.h_ascii('MART', 1000)
        tram = hash_functions.h_ascii('TRAM', 1000)
        self.assertEqual(mart, tram)
        zeros = hash_functions.h_ascii('00000', 1000)
        self.assertEqual(zeros, 240)

    def test_h_rolling(self):
        mart = hash_functions.h_rolling('MART', 1000)
        tram = hash_functions.h_rolling('TRAM', 1000)
        self.assertNotEqual(mart, tram)
        zeros = hash_functions.h_rolling('00000', 1000)
        self.assertEqual(zeros, 608)

    def test_h_binning(self):
        mart = hash_functions.h_binning('MART', 1000)
        tram = hash_functions.h_binning('TRAM', 1000)
        self.assertNotEqual(mart, tram)
        zeros = hash_functions.h_binning('00000', 1000)
        self.assertEqual(zeros, 744)

    def test_h_weighted(self):
        mart = hash_functions.h_weighted('MART', 1000)
        tram = hash_functions.h_weighted('TRAM', 1000)
        self.assertNotEqual(mart, tram)
        zeros = hash_functions.h_weighted('00000', 1000)
        self.assertEqual(zeros, 480)


if __name__ == '__main__':
    unittest.main()
