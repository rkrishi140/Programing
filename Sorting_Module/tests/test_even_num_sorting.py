"""
This is the testing module that tests the test_even_num_sorting.
"""

from Programing.Sorting_Module.even_num_sorting import quickSort
import unittest


class test_even_number_sorting(unittest.TestCase):

    def test_list_has_odd_elements(self):
        input_list = [1, 3, 7, 9, 11, 19]
        expected_output = [1, 3, 7, 9, 11, 19]
        self.assertEqual(quickSort(input_list), expected_output)

    def test_list_has_even_elements(self):
        input_list = [2, 8, 6, 12, 4, 0]
        expected_output = [0, 2, 4, 6, 8, 12]
        self.assertEqual(quickSort(input_list), expected_output)

    def test_list_has_mix_even_odd_elements(self):
        input_list = [2, 3, 7, 0, 12, 8]
        expected_output = [0, 3, 7, 2, 8, 12]
        self.assertEqual(quickSort(input_list), expected_output)