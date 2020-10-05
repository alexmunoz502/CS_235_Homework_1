CS_235_Homework_1 : Alex Munoz


DESCRIPTION
Graphs the running times of insertion sort and merge sort algorithms that sort data from a text file in descending order.


FILES

file_handler.py 
Wraps the reading/writing of code to text files into functions that can be called from outside of the file.

algorithms.py 
Contains the functions for the insertion sort and merge sort algorithms

insertsort.py and mergesort.py
These use the file_handler.py and algorithms.py functions to read data from the data.txt file, sort the data, and then write the data out to their respective '.out' files.