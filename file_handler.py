def read_data_from_file(file_name : str) -> list:
    """
    DESCRIPTION
    Reads the number data from a specified file, the
    format which has the first number indicating the number
    of elements in the list, and the following numbers representing
    the elements in the list.

    PARAMETERS
    file_name: the specified file from which to read the data

    RETURN
    Returns a list of lists, each list being one line from the data file
    """

    data_list = []

    with open(file_name, "r") as data_file:
        for line in data_file:
            line_numbers = line.split()
            # add line to data list, ignore element 0, not needed for python
            data_list.append([int(number) for number in line_numbers[1:]])

    return data_list
            
def write_data_to_file(data : list, file_name : str) -> None:
    """
    DESCRIPTION
    Writes sorted list data to a specified filename. The data
    will be written in the format {list size} {elements}
    for example a list of [1, 2, 3] will be written as:
    3 1 2 3
    each line in the file will correlate to a list in the data 
    parameter

    PARAMETERS
    data: a list of lists of numbers that have been sorted
    file_name: the name of the file to save the data to

    RETURN
    no return
    """

    with open(file_name, "w") as data_file:
        for number_list in data:
            file_line = ' '.join([str(i) for i in number_list]) + '\n'
            data_file.write(file_line)