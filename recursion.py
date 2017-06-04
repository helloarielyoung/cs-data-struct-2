# --------- #
# Recursion #
# --------- #

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """
    if i < len(my_list):
        print my_list[i]
        i += 1
        print_item(my_list, i)


# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """

    # Maybe I am learning something.  Realized this better solution after
    # finishing all the rest of the assignment
    print tree.data

    for child in tree.children:
        print_all_tree_data(child)

    #Here was my first answer, which works but I guess is way overly complicated
    # if type(tree) == list:
    #     to_visit = tree
    # else:
    #     to_visit = [tree]

    # current = to_visit.pop(0)
    # print current.data

    # to_visit.extend(current.children)

    # if to_visit:
    #     print_all_tree_data(to_visit)


# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """

    if not my_list:
        return 0
    return 1 + list_length(my_list[1::2]) + list_length(my_list[2::2])

    # I am really lost on this.  I tried for an hour unsuccessfully to do this by
    # myself.  Finally googled the answer above.  I don't understand why it
    # works.  I also don't understand why this doesn't work:
    # if not my_list:
    #     return 0
    # return 1 + my_list[1:]


# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
        >>> four = Node(4)
        >>> five = Node(5)
        >>> two.add_child(four)
        >>> two.add_child(five)
        >>> num_nodes(one)
        5
        >>> six = Node(6)
        >>> three.add_child(six)
        >>> num_nodes(one)
        6
    """

    count = 1
    for child in tree.children:
        count += num_nodes(child)
    return count


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
