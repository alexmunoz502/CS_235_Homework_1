import math

def insertion_sort(number_list : list) -> None:
    """
    DESCRIPTION
    Alters a list of integers, sorting its elements in descending order.

    PARAMETERS
    number_list: The list of numbers to sort

    RETURN
    no return
    """

    for index in range(1, len(number_list)):
        key = number_list[index]
        position = index - 1
        while position >= 0 and number_list[position] < key:
            number_list[position + 1] = number_list[position]
            position -= 1
        number_list[position + 1] = key

def merge_sort(number_list : list) -> None:
    """
    DESCRIPTION
    Alters a list of integers, sorting its elements in descending order.

    PARAMETERS
    number_list: The list of numbers to sort

    RETURN
    no return
    """
    recursive_merge_sort(number_list, 0, len(number_list))


def recursive_merge_sort(number_list : list, start_index : int, end_index : int) -> None:
    """
    DESCRIPTION
    A recursive function that splits a list in two, and combines the sorted values

    PARAMETERS
    number_list: The list of numbers to sort
    start_index: The index to start the split at
    end_index: The index to end the split at

    RETURN
    no return
    """
    if (end_index - start_index) > 1:
        middle_index = (start_index + end_index) // 2
        recursive_merge_sort(number_list, start_index, middle_index)
        recursive_merge_sort(number_list, middle_index, end_index)
        merge(number_list, start_index, middle_index, end_index)

def merge(number_list : list, start_index : int, middle_index : int, end_index : int) -> None:
    """
    DESCRIPTION
    sorts the values of two sublists and merges them in sorted order
    into the original list

    PARAMETERS
    number_list: The list of numbers to sort
    start_index: The index to start the left list at
    middle_index: The index to end the left list at and start the right list at
    end_index: The index to end the right list at

    RETURN
    no return
    """
    left = number_list[start_index : middle_index]
    right = number_list[middle_index : end_index]

    # Use negative infinity as sentinel values
    left.append(-math.inf)
    right.append(-math.inf)

    left_index = 0
    right_index = 0
    for index in range(start_index, end_index):
        if left[left_index] >= right[right_index]:
            number_list[index] = left[left_index]
            left_index += 1
        else:
            number_list[index] = right[right_index]
            right_index += 1
