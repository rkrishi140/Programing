"""
This module helps to sort the even number in a list and position of the odd numbers remains as it is.

Example:
    To run this module we need to go in their directory and run the following command
    $ python QuickSort.py

Attributes:
    There is no module level variables are declared.

Todo:
    Only applicable for integer containing list.

"""
from Programing.Sorting_Module.sortinglog import my_logger


def toFindPivotIndex(inputList, leftIndex, rightIndex):
    """
    Last element of the list is being considered as pivot element.
    Args:
        param1 (list): inputList: input list
        param2 (list): leftIndex:  leftmost index of the input list
        param3 (list): rightIndex: rightmost index of the input list
    Returns:
        int: Returns index of pivot element.
    """
    pivotElementIndex = leftIndex - 1
    pivotElement = inputList[rightIndex - 1]

    # j is the iterator of input list
    for j in range(leftIndex, rightIndex - 1):
        # Comparision with pivot element
        if inputList[j] <= pivotElement:
            pivotElementIndex += 1
            # Applying swapping
            inputList[pivotElementIndex], inputList[j] = inputList[j], inputList[pivotElementIndex]
    inputList[pivotElementIndex + 1], inputList[rightIndex - 1] = inputList[rightIndex - 1], inputList[
        pivotElementIndex + 1]
    return pivotElementIndex + 1


def quickSort1(inputList, leftIndex, rightIndex):
    """
    After getting the pivot element's index, quickSort1 function is called recursively for both part pivotElementIndex.e
    right and left side of the pivot element.
    :param inputList: input list
    :param leftIndex:  leftmost index of the input list
    :param rightIndex: rightmost index of the input list
    :return:  List gets sorted(increasing order)
    """
    # Termination condition of recursive call
    if leftIndex < rightIndex:
        index = toFindPivotIndex(inputList, leftIndex, rightIndex)
        # quickSort1() is recursively called to the left of index
        quickSort1(inputList, leftIndex, index)
        # quickSort1() is recursively called to the right of index
        quickSort1(inputList, index + 1, rightIndex)


def quickSort(input_list):
    even_input_list = []
    for i, j in enumerate(input_list):
        if j % 2 == 0:
            even_input_list.append(j)

    my_logger.debug('Entered in to helping function of quick sort for input list {}'.format(input_list))
    """
    To call the quickSort1() i.e a helping function.
    Args:
        param1 (list): list to be sorted
    Returns:
         list: Returns sorted list
    """
    try:
        my_logger.debug('Entered into main try block of QuickSort to sort {} list'.format(input_list))
        quickSort1(even_input_list, 0, len(even_input_list))
        print(even_input_list)
        o = 0
        for l, _ in enumerate(input_list):
            if input_list[l] % 2 == 0:
                input_list[l] = even_input_list[o]
                o += 1
    except TypeError as t:
        my_logger.error('Error Occurred and type of error is {}'.format(my_logger.exception(t)))
    else:
        my_logger.debug('Output Sorted List is: {} by Quick Sort'.format(input_list))
        return input_list

