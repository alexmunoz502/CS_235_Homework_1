import file_handler
import algorithms

# CONSTANTS
FILE_PATH = "data.txt"
INSERT_OUT_PATH = "insert.out"
MERGE_OUT_PATH = "merge.out"


data_list = file_handler.read_data_from_file(FILE_PATH)
insert_sort_list = [line[:] for line in data_list]
merge_sort_list = [line[:] for line in data_list]

for number_list in insert_sort_list:
    algorithms.insertion_sort(number_list)

for number_list in merge_sort_list:
    algorithms.merge_sort(number_list)

file_handler.write_data_to_file(insert_sort_list, INSERT_OUT_PATH)
file_handler.write_data_to_file(merge_sort_list, MERGE_OUT_PATH)