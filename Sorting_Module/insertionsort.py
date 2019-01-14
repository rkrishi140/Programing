"""------------Insertion Sorting-----------------

It performs insertion sorting on a input list where input list may contain integer or float or char/string.


Attributes:
    No module level attributes are declared in this module.

Todo:
    Sorting for Input tuple is to be performed.

"""
from Sorting_Module.LogSorting import logger


def insertion_sort(l_input):
    """ In this method we sort a sublist(starting from 0 index) with addition of one more element till the whole list is
     sorted.
     Args:
         l_input(list) : Input List

     Return:
         list : Sorted List
    """

    # noinspection PyBroadException

    try:
        length = len(l_input)

        for i in range(1, length):
            # Key is next element of the element till the sublist is sorted.
            key = l_input[i]
            j = i - 1
            # Moving one position ahead if key is less than any of the element in Sorted sublist.
            while j >= 0 and l_input[j] > key:
                l_input[j + 1] = l_input[j]
                j = j - 1
            l_input[j + 1] = key
    except Exception as Error:
        logger.error('{}'.format(Error))
    else:
        logger.info("Quick Sort for input list: {} ran successfully".format(l_input))
        return l_input


if __name__ == '__main__':
    unSortedList = ["sa", "ra"]
    SortedList = insertion_sort(unSortedList)
    print(SortedList)
