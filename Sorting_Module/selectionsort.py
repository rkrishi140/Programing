"""------------Selection Sorting-----------------

It performs selection sorting on a input list where input list may contain integer or float.


Attributes:
    No module level attributes are declared in this module.

Todo:
    Sorting for Input list with character is to be performed.

"""


def selection_sort(l_input):
    """In this method we will find  the minimum element and swap with element against the minimum index.
    We will continue this process till the whole list is sorted

    Args:
        l_input (list) : Input List

    Return:
        list : Sorted List
    """
    length = len(l_input)

    # Loop for finding the minimum element and swap with element which is on index of element in Sorted List(If Sorted).
    for i, _ in enumerate(l_input):
        for j in range(i+1, length):
            if l_input[j] < l_input[i]:
                # Swapping of element if there is any bigger element before smaller list.
                l_input[i], l_input[j] = l_input[j], l_input[i]

    return l_input


if __name__ == '__main__':
    unSortedList = [-3.4, 2.5, 4.5, -2]
    SortedList = selection_sort(unSortedList)
    print(SortedList)
