import algorithms
import file_handler

# Constants
FILE_PATH = "data.txt"
MERGE_OUT_PATH = "merge.out"

if __name__ == "__main__":
    data_list = file_handler.read_data_from_file(FILE_PATH)

    for number_list in data_list:
        algorithms.merge_sort(number_list)

    file_handler.write_data_to_file(data_list, MERGE_OUT_PATH)