#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    # outer loop length of the list minus 1 (unless no swap)
    for i in range(len(lst) - 1):
        swap_occurred = False 
        # inner loop:
        # length of the list minus 1
        # will go all the way through the list once and highest item will be
        # at the end.  If no swap occurred during iteration, list is sorted
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                # if one to the right is smaller, swap them
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap_occurred = True
        if not swap_occurred:
            # if no swap, list is done
            break

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    final_list = []

    # reverse the lists in order to get O(n) runtime
    list1 = list1[::-1]
    list2 = list2[::-1]

    # while either list is greater than zero in length
    while len(list1) > 0 or len(list2) > 0:
        # if list 1 is empty, pop from end of list2
        if list1 == []:
            final_list.append(list2.pop())
        # if list 2 is empty, pop from end of list1
        elif list2 == []:
            final_list.append(list1.pop())
        # if last one in list1 is less than last one in list 2, pop list1
        elif list1[-1] < list2[-1]:
            final_list.append(list1.pop())
        # otherwise, last one in list2 must be less than last one in list1
        # so pop that one
        else:
            final_list.append(list2.pop())
        # repeats if either list is not empty

    return final_list

##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    if len(lst) < 2:
        return lst

    mid = int(len(lst) // 2)
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge_lists(left, right)

    # I am confused because the merge_sort example in "sorting-demo\sorts.py"
    # does not return anything...  how does that work??

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
