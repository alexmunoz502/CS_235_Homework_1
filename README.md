## Timing Sorting Algorithms
##### Python Scripts for Analyzing Sorting Algorithm Runtimes


###### DESCRIPTION

There are two main functionalities to the scripts in this project:

1. Sorting: these scripts can be used to sort a data file containing integers
in _descending_ order, and output their results to a new file.  

2. Timing: these scripts can be used to evaluate the average time it takes for
an algorithm to sort a number of large arrays.  

###### FILES

*data.txt*  
This file contains the data that will be read by the sorting scripts. Each 
new line in the file will be read as a separate array. Each line contains
integers delimited by a space character.

*insert_sort.py* and *merge_sort.py*  
These read data from the data.txt file, sort the data in _descending_ order, 
and then write the sorted data out to *insert.out* and *merge.out*, 
resepectively. 

*file_handler.py*  
A set of basic file-handling functions for the reading/writing of text 
files that can be called by the other scripts in this project.

*algorithms.py*  
Contains the functions for the insertion sort and merge sort algorithms.

*insert_time.py* and *merge_time.py*  
These get the average runtime for an algorithm for list sizes of N. Optional
argument can be provided to override the default sample size of 3.  
  Example:  
  `py merge_time.py 5`  
  The results will be logged to the terminal. NOTE: This process can take some 
time, it is recommended to keep the sample size under 10.

*algo_timer.py*  
This function generates a list of randomly generated numbers and has a 
reference to a specified sorting algorithm that is called and timed.