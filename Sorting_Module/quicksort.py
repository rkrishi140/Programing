"""
This is QuickSort module which contains quickSort method. Which performs sorting on given list,
list is having only integer type element.

Pivot element can be at any position like at mid, at leftmost, at rightmost,...etc. But in our case pivot element is
considered at right most position. After considering the pivot element, it is compared with each element and its
location is assigned in such a way that left side and right side elements are lesser and greater than the pivot
element and then index of this pivot element is returned.

Example:
    To run this module we need to go in their directory and run the following command
    $ python QuickSort.py

Attributes:
    There is no module level variables are declared.

Todo:
    Only applicable for integer containing list.

"""
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    filename='Sort.log'
                    )


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
    logging.debug('Entered in to helping function!')
    """
    To call the quickSort1() i.e a helping function.
    Args:
        param1 (list): list to be sorted
    Returns:
         list: Returns sorted list
    """
    try:
        logging.debug('Entered into main try block!')
        quickSort1(input_list, 0, len(input_list))
    except TypeError as t:
        logging.error('Error Occurred and type of error is {}'.format(logging.exception(t)))
    else:
        logging.info('Try else block executed!')
        logging.debug('Output Sorted List is: {}'.format(input_list))
        return input_list


if __name__ == '__main__':
    l_unsorted = [1, 3, 5, 3, 2, 8, 7, 0]
    l_sorted = quickSort(l_unsorted)
