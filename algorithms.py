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
    recursive_merge_sort(number_list, 0, len(number_list)-1)


def recursive_merge_sort(number_list, start_index, end_index):
    if start_index < end_index:
        middle_index = (start_index + end_index) // 2
        recursive_merge_sort(number_list, start_index, middle_index)
        recursive_merge_sort(number_list, middle_index + 1, end_index)
        merge(number_list, start_index, middle_index, end_index)

def merge(number_list, start_index, middle_index, end_index):
    left_end_index = middle_index - start_index
    right_end_index = end_index - middle_index
    left_hand = []
    right_hand = []
    for i in range(0, left_end_index):
        left_hand.append(number_list[start_index + i])
    for j in range(0, right_end_index):
        right_hand.append(number_list[middle_index + j])

    print("Merging: " + str(left_hand) + " " + str(right_hand))

    left_hand.append(math.inf)
    right_hand.append(math.inf)

    

    left_index = 0
    right_index = 0
    for index in range(start_index, end_index):
        if left_hand[left_index] <= right_hand[right_index]:
            number_list[index] = left_hand[left_index]
            left_index += 1
        else:
            number_list[index] = right_hand[right_index]
            right_index += 1
    

