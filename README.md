CS_235_Homework_1 : Alex Munoz


DESCRIPTION
1. Sorts a list of number values from a file called data.txt, each line in the data file must contain only integers, & the first number being the size of the list. The data.txt file must be in the same directory

2. Calculates the running times of insertion sort and merge sort algorithms that sort data from randomly generated lists of size N. The results are printed to the console. NOTE: I used a sample size of 10 for my written homework submission, but reduced it to 2 so it will run faster for the TAs


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