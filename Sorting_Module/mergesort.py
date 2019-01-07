"""
This is MergeSort module which contains mergeSort method. Which performs sorting on given list,
list is having only integer type element.

Example:
    To run this module we need to go in their directory and run the following command
    $ python MergeSort.py

Attributes:
    There is no module level variables are declared. Only sys package is imported to get the maxsize in the program.
    Reason is written below the method's doc string.

Todo:
    Only applicable for integer containing list.

"""


import sys
from Programing.Sorting_Module.sortinglog import my_logger


def mergeSort(inputList):
    """
    Recursively this function is called to sort inputList list.
    To reduce the number of comparision, at the end of the List(s) maxsize of the integer is being append.
    Args:
    param1 (list): inputList: This is first argument type of it is list(to be sorted.)

    Returns:
        list: Returns the sorted list.
    """
    try:
        # Termination condition if size of list is 1
        if len(inputList) > 1:
            midIndex = len(inputList) // 2
            # leftList is left part from the midIndex
            leftList = inputList[:midIndex]
            # rightList is right part from the midIndex
            rightList = inputList[midIndex:]
            # Recursive call
            mergeSort(leftList)
            mergeSort(rightList)
            # Appending large integer value at the end of both the lists to reduce no. of comparisons
            leftList.append(sys.maxsize)
            rightList.append(sys.maxsize)
            leftListIterator = 0
            rightListIterator = 0
            # Merging is being done, k is the iterator of the inputList
            for k, _ in enumerate(inputList):
                if leftList[leftListIterator] > rightList[rightListIterator]:
                    inputList[k] = rightList[rightListIterator]
                    rightListIterator += 1
                else:
                    inputList[k] = leftList[leftListIterator]
                    leftListIterator += 1
    except TypeError as t:
        my_logger.error('Error Occurred and type of error is {}'.format(my_logger.exception(t)))
    else:
        my_logger.debug('Recursively Sorted list is {} by merge sort'.format(inputList))
        return inputList


if __name__ == '__main__':
    l_unsorted = [1, 3, 5, 3, 2, 8, 7, 0]
    l_sorted = mergeSort(l_unsorted)