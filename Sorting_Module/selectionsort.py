"""
This is SelectionSort module which contains selectionSort method. Which performs sorting on given list,
list is having only integer type element.


Example:
    To run this module we need to go in their directory and run the following command
    $ python SelectionSort.py

Attributes:
    There is no module level variables are declared.

Todo:
    Only applicable for integer containing list so character containing list to be done.

"""
from Programing.Sorting_Module.sortinglog import my_logger


def findMinIndex(inputList, leftIndex, rightIndex):
    """
    This function finds the minimum element's position in inputList.
    Args:
        param1 (list): inputList: input list to be sorted
        param2 (int): leftIndex: leftmost index of the list
        param3 (int): rightIndex: rightmost index of the list

    Returns:
        int: index of minimum element in the list.

    """
    minIndex = leftIndex
    # i is the iterator of the inputList and finds the minimum element index
    for i in range(leftIndex, rightIndex):
        if inputList[minIndex] >= inputList[i]:
            minIndex = i
    return minIndex


def selectionSort(inputList):
    """
    Minimum element  find from the unsorted part of the list and then after it is placed at first position of unsorted
    list.
    Args:
        param1 (list): input list to be sorted

    Returns:
        list: Sorted list is returned

    """
    try:
        for i, _ in enumerate(inputList):
            index = findMinIndex(inputList, i, len(inputList))
            # Applying swapping approach
            inputList[i], inputList[index] = inputList[index], inputList[i]
    except TypeError as t:
        my_logger.error('Error Occurred and type of error is {}'.format(my_logger.exception(t)))

    except BaseException as be:
        my_logger.error('To sort {} list occurred this error {}'.format(inputList, be))
    else:
        my_logger.debug('Output Sorted List is: {} by selection sort'.format(inputList))
        return inputList


if __name__ == '__main__':
    l_unsorted = [1, 3, 5, 3, 2, 8, 7, 0]
    l_sorted = selectionSort(l_unsorted)