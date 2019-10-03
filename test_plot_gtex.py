import unittest
import random
import data_viz
import plot_gtex
import numpy as np
import os


class TestPlotGtex(unittest.TestCase):
    def test_boxplot(self):
        datapoints = 1000

        normal = np.random.normal(1, 1, datapoints)
        uniform = np.random.uniform(1, 1, datapoints)

        data = [normal, uniform]
        data_viz.boxplot(data, ['Normal', 'Uniform'], 'Distributions',
                         'Distribution', 'y-value', 'testplot.png')

        self.assertTrue(os.path.exists('testplot.png'))
        os.remove('testplot.png')

    def test_linear_search(self):
        array = np.random.rand(50, 1)

        found = plot_gtex.linear_search(array[0], array)
        self.assertEqual(0, found)

        r = plot_gtex.linear_search(100, array)
        self.assertEqual(r, -1)

    def test_binary_search(self):
        array = [['cat', 1], ['dog', 2]]

        found = plot_gtex.binary_search('cat', array)
        self.assertEqual(1, found)

        r = plot_gtex.linear_search('pigeon', array)
        self.assertEqual(r, -1)


if __name__ == '__main__':
    unittest.main()
