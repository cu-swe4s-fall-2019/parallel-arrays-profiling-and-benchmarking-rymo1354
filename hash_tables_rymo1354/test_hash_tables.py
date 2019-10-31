import unittest
import os
import hash_tables
import hash_functions


class TestHashTables(unittest.TestCase):
    def test_reservoir_sampling(self):
        V = [1, 2, 3, 4, 5]
        val_in_V = False
        hash_tables.reservoir_sampling('val', 5, V)
        if 'val' in V:
            val_in_V = True
        self.assertEqual(val_in_V, True)

        V = [1, 2, 3, 4, 5]
        hash_tables.reservoir_sampling('val', 6, V)
        self.assertEqual('val', V[5])

    def test_linear_probing(self):
        HT = hash_tables.LinearProbe(1000, hash_functions.h_ascii)
        HT.add('MART', 'MART')
        HT.add('TRAM', 'TRAM')
        self.assertEqual(HT.search('MART'), 'MART')
        self.assertEqual(HT.search('TRAM'), 'TRAM')
        self.assertEqual(HT.search('TARMAC'), None)

        HT = hash_tables.LinearProbe(1000, hash_functions.h_rolling)
        HT.add('MART', 'MART')
        HT.add('TRAM', 'TRAM')
        self.assertEqual(HT.search('MART'), 'MART')
        self.assertEqual(HT.search('TRAM'), 'TRAM')
        self.assertEqual(HT.search('TARMAC'), None)

        HT = hash_tables.LinearProbe(1000, hash_functions.h_weighted)
        HT.add('MART', 'MART')
        HT.add('TRAM', 'TRAM')
        self.assertEqual(HT.search('MART'), 'MART')
        self.assertEqual(HT.search('TRAM'), 'TRAM')
        self.assertEqual(HT.search('TARMAC'), None)

        HT = hash_tables.LinearProbe(1000, hash_functions.h_binning)
        HT.add('MART', 'MART')
        HT.add('TRAM', 'TRAM')
        self.assertEqual(HT.search('MART'), 'MART')
        self.assertEqual(HT.search('TRAM'), 'TRAM')
        self.assertEqual(HT.search('TARMAC'), None)

    def test_chained_hash(self):
        HT = hash_tables.ChainedHash(1000, hash_functions.h_ascii)
        HT.add('MART', 'MART')
        HT.add('TRAM', 'TRAM')
        self.assertEqual(HT.search('MART'), 'MART')
        self.assertEqual(HT.search('TRAM'), 'TRAM')
        self.assertEqual(HT.search('TARMAC'), None)

        HT = hash_tables.ChainedHash(1000, hash_functions.h_rolling)
        HT.add('MART', 'MART')
        HT.add('TRAM', 'TRAM')
        self.assertEqual(HT.search('MART'), 'MART')
        self.assertEqual(HT.search('TRAM'), 'TRAM')
        self.assertEqual(HT.search('TARMAC'), None)

        HT = hash_tables.ChainedHash(1000, hash_functions.h_weighted)
        HT.add('MART', 'MART')
        HT.add('TRAM', 'TRAM')
        self.assertEqual(HT.search('MART'), 'MART')
        self.assertEqual(HT.search('TRAM'), 'TRAM')
        self.assertEqual(HT.search('TARMAC'), None)

        HT = hash_tables.ChainedHash(1000, hash_functions.h_binning)
        HT.add('MART', 'MART')
        HT.add('TRAM', 'TRAM')
        self.assertEqual(HT.search('MART'), 'MART')
        self.assertEqual(HT.search('TRAM'), 'TRAM')
        self.assertEqual(HT.search('TARMAC'), None)


if __name__ == '__main__':
    unittest.main()
