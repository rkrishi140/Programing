"""
This is unit testing file for different - different sorting algorithms.

Attributes:
    Import of unittest and Sorting_Module


ToDo:
  Uses of OOPs concept supported by unittest like testSuite ,tear Down ,testRunner etc. More testCases to be added.

"""
import unittest
from Sorting_Module.sorting import Sort


class TestSort(unittest.TestCase):
    """ It is inheriting the TestCase Module of unittest.

    --------Unit Testing on class CallSort-----
    Args:
        unittest.TestCase : Inheriting from the unittest.
    Return:
        result : sorted list with time .
    """
    def setUp(self):
        self.unSortedList = Sort([1, 9, 8, 3, 5])
        self.emptyList = Sort([])
        self.singleItem = Sort([7])
        self.twoItem = Sort([3, 1])
        self.twoItemSorted = Sort([1, 3])
        self.listWithZero = Sort([10, 0])
        self.oddNumberItems = Sort([5, 1, 9, 2, 10])
        self.evenNumberItems = Sort([5, 1, 9, 2, 10, 11])
        self.duplicateItems = Sort([1, 2, 2, 1, 0, 0, 15, 15])
        self.largeItems = Sort([135604, 1000000, 45, 78435, 456219832, 2, 546])

    def test_unSortedList(self):
        """Testing the unSortedList"""
        correct_output = [1, 3, 5, 8, 9]
        self.assertEqual(self.unSortedList.selection_sort(), correct_output)
        self.assertEqual(self.unSortedList.insertion_sort(), correct_output)
        self.assertEqual(self.unSortedList.merge_sort(), correct_output)
        self.assertEqual(self.unSortedList.quick_sort(), correct_output)

    def test_emptyList(self):
        """Testing the emptyList"""
        correct_output = []
        self.assertEqual(self.emptyList.selection_sort(), correct_output)
        self.assertEqual(self.emptyList.insertion_sort(), correct_output)
        self.assertEqual(self.emptyList.merge_sort(), correct_output)
        self.assertEqual(self.emptyList.quick_sort(), correct_output)

    def test_singleItem(self):
        """
        Testing the list with one element.

        Return:
            bool (true or false)
        """
        correct_output = [7]
        self.assertEqual(self.singleItem.selection_sort(), correct_output)
        self.assertEqual(self.singleItem.insertion_sort(), correct_output)
        self.assertEqual(self.singleItem.merge_sort(), correct_output)
        self.assertEqual(self.singleItem.quick_sort(), correct_output)

    def test_twoItem(self):
        """
        Testing the list containing two element.

        Return:
            bool (true or false)
        """
        correct_output = [1, 3]
        self.assertEqual(self.twoItem.selection_sort(), correct_output)
        self.assertEqual(self.twoItem.insertion_sort(), correct_output)
        self.assertEqual(self.twoItem.merge_sort(), correct_output)
        self.assertEqual(self.twoItem.quick_sort(), correct_output)

    def test_twoItemSorted(self):
        """
        Testing the list which contains two element on sorted order.

        Return:
            bool (true or false)
        """
        correct_output = [1, 3]
        self.assertEqual(self.twoItemSorted.selection_sort(), correct_output)
        self.assertEqual(self.twoItemSorted.insertion_sort(), correct_output)
        self.assertEqual(self.twoItemSorted.merge_sort(), correct_output)
        self.assertEqual(self.twoItemSorted.quick_sort(), correct_output)

    def test_listWithZero(self):
        """
        Testing the list which contains zero as a element.

        Return:
            bool (true or false)
        """
        correct_output = [0, 10]
        self.assertEqual(self.listWithZero.selection_sort(), correct_output)
        self.assertEqual(self.listWithZero.insertion_sort(), correct_output)
        self.assertEqual(self.listWithZero.merge_sort(), correct_output)
        self.assertEqual(self.listWithZero.quick_sort(), correct_output)

    def test_oddNumberItems(self):
        """
        Testing the list which contains odd number of elements.

        Return:
            bool (true or false)
        """
        correct_output = [1, 2, 5, 9, 10]
        self.assertEqual(self.oddNumberItems.selection_sort(), correct_output)
        self.assertEqual(self.oddNumberItems.insertion_sort(), correct_output)
        self.assertEqual(self.oddNumberItems.merge_sort(), correct_output)
        self.assertEqual(self.oddNumberItems.quick_sort(), correct_output)

    def test_evenNumberItems(self):
        """
        Testing the list which contains even no of elements.

        Return:
            bool (true or false)

        """
        correct_output = [1, 2, 5, 9, 10, 11]
        self.assertEqual(self.evenNumberItems.selection_sort(), correct_output)
        self.assertEqual(self.evenNumberItems.insertion_sort(), correct_output)
        self.assertEqual(self.evenNumberItems.merge_sort(), correct_output)
        self.assertEqual(self.evenNumberItems.quick_sort(), correct_output)

    def test_duplicateItems(self):
        """
        Testing the list which contains duplicate element.

        Return:
            bool (true or false)
        """
        correct_output = [0, 0, 1, 1, 2, 2, 15, 15]
        self.assertEqual(self.duplicateItems.selection_sort(), correct_output)
        self.assertEqual(self.duplicateItems.insertion_sort(), correct_output)
        self.assertEqual(self.duplicateItems.merge_sort(), correct_output)
        self.assertEqual(self.duplicateItems.quick_sort(), correct_output)

    def test_largeItems(self):
        """
        Testing the list which contains large elements.

        Return:
            bool (true or false)
        """
        correct_output = [2, 45, 546, 78435, 135604, 1000000, 456219832]
        self.assertEqual(self.largeItems.selection_sort(), correct_output)
        self.assertEqual(self.largeItems.insertion_sort(), correct_output)
        self.assertEqual(self.largeItems.merge_sort(), correct_output)
        self.assertEqual(self.largeItems.quick_sort(), correct_output)


if __name__ == '__main__':
    unittest.main()
