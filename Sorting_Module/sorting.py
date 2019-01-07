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
import functools
import time
import logging
from Programs.Programing.Sorting_Module import quicksort as QuickSort
from Programs.Programing.Sorting_Module import insertionsort as InsertionSort
from Programs.Programing.Sorting_Module import mergesort as MergeSort
from Programs.Programing.Sorting_Module import selectionsort as SelectionSort


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    filename='Sort.log'
                    )


def toMeasureExecutionTime(func):
    """
    This is a decorator function that takes original function as an argument.
    Args:
        param1 (function_type):  Original function which is to be decorated

    Returns:
    function_type: Returns wrapper function i.e on hold
    """
    """ This wraps the metadata of the original function"""

    @functools.wraps(func)
    def wrapperOf_toMeasureExecutionTime_decorator(*args, **kwargs):
        """
        This is wrapping function that wrap up the task of to be decorated function.
        Args:
            param1 (args): no. of argument of the original function to be decorated
            param2 (kwargs): argument of the original function to be decorated.
        Returns:
        return_type_of_original_function: result of the original function

        """
        """ Execution time of this sorting is very fast i.e difference of time.time() is tends to zero. To get the
            significant figure using timer """
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(func.__name__ + " is taking " + str((end - start) * 1000) + " mil seconds")
        return res

    return wrapperOf_toMeasureExecutionTime_decorator


class Sort:
    """
    This class containing all the calling methods that sorts input list.
    """

    def __init__(self, inputList):
        logging.info('Object is being created!')
        self.inputList = inputList

    @property
    @toMeasureExecutionTime
    def quickSort(self):
        """ To call quickSort method """
        logging.info('QuickSort in called!')
        sorted_list = QuickSort.quickSort(self.inputList)
        return sorted_list

    @property
    @toMeasureExecutionTime
    def mergeSort(self):
        """ To call mergeSort method """
        logging.info('MergeSort is called!')
        sorted_list = MergeSort.mergeSort(self.inputList)
        return sorted_list

    @property
    @toMeasureExecutionTime
    def selectionSort(self):
        """ To call selectionSort method """
        logging.info('SelectionSort in called!')
        sorted_list = SelectionSort.selectionSort(self.inputList)
        return sorted_list

    @property
    @toMeasureExecutionTime
    def insertionSort(self):
        """ To call insertionSort method """
        logging.info('InsertionSort in called!')
        sorted_list = InsertionSort.insertionSort(self.inputList)
        return sorted_list


if __name__ == '__main__':
    input_list = [1, 4, 6, 4, 0]
    s_object = Sort(input_list)
    print(s_object.mergeSort)