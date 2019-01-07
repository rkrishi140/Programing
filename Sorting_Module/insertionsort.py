"""
This is InsertionSort.py doc string that contains sorting(insertion Sort) methods. To get the doc string we need
to run the command like.

Output: That gives the doc string of this module.
just above the logical statements comments are written.

Example:
    To run this module we need to go in their directory and execute the following commands
     $ python InsertionSort.py

Attributes:
    There is no module level variables are declared.

Todo:
    If list contains a character that needs to be done.
"""
from Programing.Sorting_Module.sortinglog import my_logger


def insertionSort(inputList):
    my_logger.info('Insertion Sort is being called for input list: {}'.format(inputList))
    """
    Left part of the list is already sorted and right side of the list is traversed in such a way that each element
    is compared with sorted list element and that element is placed at his respective position so that left list get
    sorted.

    Args:
        param1 (list): This is first parameter and type of it is list.

    Returns:
        list: This method returns sorted list.
        :param inputList:
    """
    try:
        my_logger.debug('Entered into main try block of Insertion Sort!')
        # i is the iterator of the inputList
        for i, _ in enumerate(inputList):
            # last index of sorted list
            lastIndexOfSortedList = i - 1
            key = inputList[i]
            """ Finds key's position in sorted list by shifting each element in sorted list until the termination 
            conditions """
            while key < inputList[lastIndexOfSortedList] and lastIndexOfSortedList >= 0:
                #
                inputList[lastIndexOfSortedList + 1] = inputList[lastIndexOfSortedList]
                lastIndexOfSortedList -= 1
            # Finally key is put at respective position
            inputList[lastIndexOfSortedList + 1] = key
    except TypeError as t:
        my_logger.error('Error Occurred and type of error is {}'.format(my_logger.exception(t)))

    except BaseException as be:
        my_logger.error('For input list {} in Insertion Sort {} exception occurred '.format(inputList, be))

    else:
        my_logger.info('Insertion Sort gives {} this list as output. '.format(inputList))
        return inputList


if __name__ == '__main__':
    l_unsorted = [1, 3, 5, 3, 2, 8, 7, 0]
    l_sorted = insertionSort(l_unsorted)
