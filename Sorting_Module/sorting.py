"""
This is main module for calling Sorting methods. This module contains all the method call statement that helps
to call each method after creating the instance of Sort class.

Example:
     To run this module go to their directory and needs to run following commands
     $ python Sort.py
     It can be run from IDE( Integrated Development Environment) like
     # >>> from Sorting.Sort import Sort
     # >>> list_to_be_sorted = list(range(100, 0, -5))
     # >>> list_object = Sort(list_to_be_sorted)
     # >>> list_object.insertionSort()
     # >>> list_to_be_sorted # Sorted list gets printed with execution time of chosen sorting methods

Attributes:
    There is no module level variables are declared only required modules are imported.

Todo:
    Only applicable for integer containing list.
"""
from Programing.Sorting_Module.utils import toMeasureExecutionTime
from Programing.Sorting_Module import quicksort as QuickSort
from Programing.Sorting_Module import insertionsort as InsertionSort
from Programing.Sorting_Module import mergesort as MergeSort
from Programing.Sorting_Module import selectionsort as SelectionSort
from Programing.Sorting_Module.sortinglog import my_logger


class Sort:
    """
    This class containing all the calling methods that sorts input list.
    """

    def __init__(self, inputList):
        my_logger.info('Object is being created for input list: {}'.format(inputList))
        self.inputList = inputList

    @property
    @toMeasureExecutionTime
    def quickSort(self):
        """ To call quickSort method """
        my_logger.info('QuickSort is to sort {}'.format(self.inputList))
        sorted_list = QuickSort.quickSort(self.inputList)
        return sorted_list

    @property
    @toMeasureExecutionTime
    def mergeSort(self):
        """ To call mergeSort method """
        my_logger.info('MergeSort is to sort {}'.format(self.inputList))
        sorted_list = MergeSort.mergeSort(self.inputList)
        return sorted_list

    @property
    @toMeasureExecutionTime
    def selectionSort(self):
        """ To call selectionSort method """
        my_logger.info('SelectionSort is to sort {}'.format(self.inputList))
        sorted_list = SelectionSort.selectionSort(self.inputList)
        return sorted_list

    @property
    @toMeasureExecutionTime
    def insertionSort(self):
        """ To call insertionSort method """
        my_logger.info('InsertionSort is called to sort {}'.format(self.inputList))
        sorted_list = InsertionSort.insertionSort(self.inputList)
        return sorted_list


if __name__ == '__main__':
    input_list = [1, 4, 6, 4, 0]
    s_object = Sort(input_list)
    s_object.insertionSort