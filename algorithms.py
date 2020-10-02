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

