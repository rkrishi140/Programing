"""------------Merge  Sorting--------------------

It performs merge sorting on a input list where input list may contain integer or float. This module contains three
function. In this we will divide the list till the element in list is 1. After it we will merge sorted sublist
accordingly.

Attributes:
    No module level attributes are declared in this module.

Todo:
    Sorting for Input list with character is to be performed.

"""


def merge_sort(l_input):
    """This method is passing the input list to merge_sort_algorithm function to  be processed

    Args:
        l_input (list) :Input List

    Return:

        list : Sorted List

    """

    length = len(l_input)

    # If length is 0 or 1 ,then no need to be sorted
    if length < 2:
        return l_input

    merge_sort_algorithm(l_input, 0, length)
    return l_input


def merge(l_input, left, mid, right):
    """This function merges two sublist in sorted order.

    Args:
         l_input (list): Input List
         left (int)    : Starting index of left sublist
         mid (int)     : Last Index of left sublist
         right (int)   : Last Index of right sublist
    Return:
         list : Sorted List
    """

    # Left Sublist
    left_list = l_input[left:mid]
    # Right Sublist
    right_list = l_input[mid:right]

    # Initialization of starting index of Merged List
    k = left
    # Initialization of starting index of left_list
    i = 0
    # Initialization of starting index of right_list
    j = 0

    # If there is elements in both the sublist
    while left + i < mid and mid + j < right:
        if left_list[i] <= right_list[j]:
            l_input[k] = left_list[i]
            i = i + 1
        else:
            l_input[k] = right_list[j]
            j = j + 1
        k = k + 1
    # If Elements are left in only left sublist or right sublist
    if left + i < mid:
        while k < right:
            l_input[k] = left_list[i]
            i = i + 1
            k = k + 1

    else:
        while k < right:
            l_input[k] = right_list[j]
            j = j + 1
            k = k + 1

    return l_input


def merge_sort_algorithm(l_input, left, right):
    """It is dividing the list in two equal part
    Args:
        l_input (list) : Input List
        left (int)     : Starting index of list/sublist
        right (int)     : Last index of list/sublist
        """

    if right - left > 1:
        # Calculating index of middle index
        mid = (left + right) // 2

        # Dividing the list
        merge_sort_algorithm(l_input, left, mid)
        merge_sort_algorithm(l_input, mid, right)

        # Merging the sublist
        merge(l_input, left, mid, right)


if __name__ == '__main__':
    unSortedList = [-1.5, -2.4, 4]
    SortedList = merge_sort(unSortedList)
    print(SortedList)
