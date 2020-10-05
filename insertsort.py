import file_handler
import algorithms
import os

# CONSTANTS
DIRECTORY = os.path.dirname(__file__)
FILE_PATH = os.path.join(DIRECTORY, "data.txt")
INSERT_OUT_PATH = os.path.join(DIRECTORY, "insert.out")

if __name__ == "__main__":
    data_list = file_handler.read_data_from_file(FILE_PATH)

    for number_list in data_list:
        algorithms.insertion_sort(number_list)

    file_handler.write_data_to_file(data_list, INSERT_OUT_PATH)
