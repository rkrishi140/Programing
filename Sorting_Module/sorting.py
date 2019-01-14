"""
It is driver module which is calling different type of sorting algorithms which are following.
1.Selection Sorting
2.Insertion Sorting
3.Quick Sorting
4.Merge Sorting

All the imported modules support input as a list and list may contain int/float or char/string.

Attributes:
    Importing different sorting algorithms.

ToDO:
    Importing more sorting algorithms.


"""
from Sorting_Module import selectionsort
from Sorting_Module import insertionsort
from Sorting_Module import quicksort
from Sorting_Module import mergesort
from Sorting_Module.utils import func_execution_time
from Sorting_Module.LogSorting import logger


class Sort:
    """
    It is accessible to all the module in this package.
    """
    def __init__(self, l_input):
        self.l_input = l_input
        logger.info('Sort instance has been created for input list {}'.format(self.l_input))

    @func_execution_time
    def selection_sort(self):
        """This method will be called for Selection Sorting"""

        sorted_list = selectionsort.selection_sort(self.l_input)
        return sorted_list

    @func_execution_time
    def insertion_sort(self):
        """This method will be called for Insertion Sorting"""
        sorted_list = insertionsort.insertion_sort(self.l_input)
        return sorted_list

    @func_execution_time
    def merge_sort(self):
        """This method will be called for Merge Sorting"""
        sorted_list = mergesort.merge_sort(self.l_input)
        return sorted_list

    @func_execution_time
    def quick_sort(self):
        """This method will be called for Quick Sorting"""
        sorted_list = quicksort.quick_sort(self.l_input)
        return sorted_list


if __name__ == '__main__':
    # unsorted_list = [1, 3, 2, 4, 7, 9]
    obj = Sort([1, 2, 4, 3, 0]).selection_sort()
    # sorted_ = obj.selection_sort()
    print(obj)
