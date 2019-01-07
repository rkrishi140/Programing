""""
This is testing call module. Which covers almost all test scenarios of all imported sorting methods.

Example:
    To run this module, need to go their directory and run the following command
    $ python test_sort.py

    Output: With execution time of each methods and covers all written test scenarios

Todo:
    Only positive test scenario has been covered remaining yet to done.

"""

from Programs.Programing.Sorting_Module.sorting import Sort
import unittest

class TestSort(unittest.TestCase):
    """
        TestSort class inherits properties from unittest.TestCase class to perform the testing.
    """

    def setUp(self):
            self.unsorted_list = Sort([3, 8, 2, 1, 9, 7, 4, 6])
            self.sorted_list = Sort([1, 2, 3, 4, 5, 6, 7, 8])
            self.reverse_sorted_list = Sort([8, 7, 6, 5, 4, 3, 2, 1])
            self.repetitive_element_list = Sort([3, 8, 2, 1, 9, 8, 4, 8])
            self.zero_size_list = Sort([])
            self.one_size_list = Sort([1])
            self.zero_element_in_list = Sort([0, 0, 3, 4, 6, 7, 8, 9])
            self.negative_elements_list = Sort([-1, -2, -3, -4, -5])

    def test_unsorted_list(self):
        """ When input list is unsorted """
        self.assertEqual(self.unsorted_list.selectionSort, [1, 2, 3, 4, 6, 7, 8, 9])
        self.assertEqual(self.unsorted_list.insertionSort, [1, 2, 3, 4, 6, 7, 8, 9])
        self.assertEqual(self.unsorted_list.quickSort, [1, 2, 3, 4, 6, 7, 8, 9])
        self.assertEqual(self.unsorted_list.mergeSort, [1, 2, 3, 4, 6, 7, 8, 9])

    def test_sorted_list(self):
        """ When input list is already sorted """
        self.assertEqual(self.sorted_list.quickSort, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(self.sorted_list.mergeSort, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(self.sorted_list.selectionSort, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(self.sorted_list.insertionSort, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_reverse_sorted_list(self):
        """ When list is sorted in reverse order """
        self.assertEqual(self.reverse_sorted_list.quickSort, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(self.reverse_sorted_list.mergeSort, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(self.reverse_sorted_list.selectionSort, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(self.reverse_sorted_list.insertionSort, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_repeated_element_list(self):
        """ When few elements are repeated in the input list"""
        self.assertEqual(self.repetitive_element_list.quickSort, [1, 2, 3, 4, 8, 8, 8, 9])
        self.assertEqual(self.repetitive_element_list.mergeSort, [1, 2, 3, 4, 8, 8, 8, 9])
        self.assertEqual(self.repetitive_element_list.selectionSort, [1, 2, 3, 4, 8, 8, 8, 9])
        self.assertEqual(self.repetitive_element_list.insertionSort, [1, 2, 3, 4, 8, 8, 8, 9])

    def test_zero_size_list(self):
        """ When size of the input list is zero """
        self.assertEqual(self.zero_size_list.quickSort, [])
        self.assertEqual(self.zero_size_list.mergeSort, [])
        self.assertEqual(self.zero_size_list.selectionSort, [])
        self.assertEqual(self.zero_size_list.insertionSort, [])

    def test_list_containing_zero(self):
        """" List containing multiple zeros """
        self.assertEqual(self.zero_element_in_list.quickSort, [0, 0, 3, 4, 6, 7, 8, 9])
        self.assertEqual(self.zero_element_in_list.mergeSort, [0, 0, 3, 4, 6, 7, 8, 9])
        self.assertEqual(self.zero_element_in_list.selectionSort, [0, 0, 3, 4, 6, 7, 8, 9])
        self.assertEqual(self.zero_element_in_list.insertionSort, [0, 0, 3, 4, 6, 7, 8, 9])

    def test_list_containing_negative_element(self):
        """ When list containing negative integers """
        self.assertEqual(self.negative_elements_list.quickSort, [-5, -4, -3, -2, -1])
        self.assertEqual(self.negative_elements_list.mergeSort, [-5, -4, -3, -2, -1])
        self.assertEqual(self.negative_elements_list.selectionSort, [-5, -4, -3, -2, -1])
        self.assertEqual(self.negative_elements_list.insertionSort, [-5, -4, -3, -2, -1])

    def test_single_element_list(self):
        """ When list size is exactly one """
        self.assertEqual(self.one_size_list.quickSort, [1])
        self.assertEqual(self.one_size_list.mergeSort, [1])
        self.assertEqual(self.one_size_list.selectionSort, [1])
        self.assertEqual(self.one_size_list.insertionSort, [1])

    def tearDown(self):
        pass