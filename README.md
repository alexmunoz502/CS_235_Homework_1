CS_235_Homework_1 : Alex Munoz


DESCRIPTION
Graphs the running times of insertion sort and merge sort algorithms that sort data from a text file in descending order.
The data.txt file must be in the same directory

FILES

insertsort.py and mergesort.py
PROBLEM #4 HOMEWORK files
These use the file_handler.py and algorithms.py functions to read data from the data.txt file, sort the data, and then write the data out to their respective '.out' files.

file_handler.py 
Wraps the reading/writing of code to text files into functions that can be called from outside of the file.

algorithms.py 
Contains the functions for the insertion sort and merge sort algorithms

insertTime.py and mergeTime.py
PROBLEM #5 HOMEWORK files
These utilize the algorithms.py and algo_timer.py functions to get the average runtime for an algorithm for list sizes of N

algo_timer.py
This function generates a list of randomly generated numbers and has a function which calls a specified sorting algorithm and times
how long it takes to run the sorting algorithm on each list of size N