import unittest
import os
import scatter


class TestScatter(unittest.TestCase):
    def test_check_path_true(self):
        open('test.csv', 'a').close()
        true = scatter.check_path('test.csv')
        self.assertEqual(True, true)
        os.system('rm test.csv')

    def test_check_path_false1(self):
        open('test.csv', 'a').close()
        os.system('chmod -r test.csv')
        false = scatter.check_path('test.csv')
        self.assertEqual(False, false)
        os.system('rm test.csv')

    def test_check_path_false2(self):
        false = scatter.check_path('test.csv')
        self.assertEqual(False, false)


if __name__ == '__main__':
    unittest.main()
