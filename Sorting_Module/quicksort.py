"""------------Quick Sorting--------------------

It performs quick sorting on a input list where input list may contain integer or float.It is also based on divide and
conquer algorithm.

Attributes:
    No module level attributes are declared in this module.

Todo::
    Sorting for Input list with character is to be performed.

"""


def quick_sort(l_input):
    """This method is passing the input list to quick function to  be processed.

    Args:
        l_input (list) : Input List

    Return:
        list : Sorted List
    """

    length = len(l_input)

    if length < 2:
        return l_input

    quick(l_input, 0, length-1)

    return l_input


def partition(l_input, low, high):
    """It will return the partitioning index from where we have to split the list.

     Args:
          l_input (list) : Input List
          low (int)      : Starting index of list/sublist
          high(int)      : Last Index of list/sublist

     Return:
         p_index (int) : The index from where the list/sublist to split.
    """

    # Initialization of partitioning index.
    p_index = low

    # Pivot is the last element of the list.
    pivot = l_input[high]

    for i in range(low, high):
        if l_input[i] <= pivot:
            # Swapping with pivot to make all smaller element than pivot in left
            # side of pivot in list and bigger in right side of pivot in list
            l_input[p_index], l_input[i] = l_input[i], l_input[p_index]
            p_index = p_index + 1

    # This is swapping to place pivot element on its
    # real place in order to make sublist/list sorted.
    l_input[p_index], l_input[high] = l_input[high], l_input[p_index]
    return p_index


def quick(l_input, low, high):
    """This function will divide list/sublist in two part from the p_index.
    After that this function will call the same function recursively till the
    condition satisfies.

    Args:
         l_input (list) : list/sublist of input list
         low (int)      : Starting index of list/sublist
         high (int)     : Last index of list/sublist
    Return:
        list : Sorted List
    """
    if low < high:
        # Calculating the p_index
        p_index = partition(l_input, low, high)

        # Calling the same function recursively.
        quick(l_input, low, p_index - 1)
        quick(l_input, p_index + 1, high)

    return l_input


if __name__ == '__main__':
    unSortedList = [-1.5, -2.4, 4]
    SortedList = quick_sort(unSortedList)
    print(SortedList)
