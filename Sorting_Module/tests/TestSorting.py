"""
It is the testing file for the  Sort Module .

ToDo:
More testcases to added .

"""
import unittest
from Sorting_Module.sorting import Sort


class TestCalling(unittest.TestCase):
    """ It is inheriting the TestCase Module of unittest.

    --------Unit Testing on class CallSort-----
    Args:
        unittest.TestCase : Inheriting from the unittest.
    Return:
        result : sorted list with time .
    """

    def test_selection_sort(self):
        """Selection Sort Testing for a list and empty list"""
        list1 = [1, 2, 3, 2, 5]
        Sort(list1).selection_sort()
        result = list1
        self.assertEqual(result, [1, 2, 2, 3, 5])
        list2 = []
        Sort(list1).selection_sort()
        result = list2
        self.assertEqual(result, [])

    def test_insert_sort(self):
        """Insertion Sort Testing for a list and empty list"""
        list1 = [1, 2, 3, 2, 5]
        Sort(list1).insert_sort()
        result = list1
        self.assertEqual(result, [1, 2, 2, 3, 5])
        list2 = []
        Sort(list1).insert_sort()
        result = list2
        self.assertEqual(result, [])

    def test_merge_sort(self):
        """Merge Sort Testing for a list and empty list"""
        list1 = [1, 2, 3, 2, 5]
        Sort(list1).merge_sort()
        result = list1
        self.assertEqual(result, [1, 2, 2, 3, 5])
        list2 = []
        Sort(list1).merge_sort()
        result = list2
        self.assertEqual(result, [])

    def test_quick_sort(self):
        """Quick Sort Testing for a list and empty list"""
        list1 = [1, 2, 3, 2, 5]
        Sort(list1).quick_sort()
        result = list1
        self.assertEqual(result, [1, 2, 2, 3, 5])
        list2 = []
        Sort(list1).quick_sort()
        result = list2
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
