import statistics
import typing
import random
import algorithms
import time

# CONSTANTS - Random Number Range
RANDOM_INT_MIN = 0
RANDOM_INT_MAX = 10000

# CONSTANT - Number of times to run timer to get average time
# NOTE: I used a sample size of 10 to get the numbers for my tables/graphs, 
#       but to run faster for the TAs I've switched this to 2.
SAMPLE_SIZE = 2

# Generate new seed to prevent the same numbers each time
random.seed()

def generate_random_values(list_size : int, min_value : int = RANDOM_INT_MIN, max_value : int = RANDOM_INT_MAX) -> list:
    """
    DESCRIPTION
    generates a list of specified length of random numbers between speficied values

    PARAMETERS
    list_size: The size of the list to generate
    min_value: The minimum value the random number generator will use (Default to RANDOM_INT_MIN constant)
    max_value: The maximum value the random number generator will use (Default to RANDOM_INT_MAX constant)

    RETURN
    returns the list of randomly generated numbers
    """
    number_list = []
    for _ in range(list_size):
        number_list.append(random.randint(min_value, max_value))
    return number_list

def time_algorithm(list_sizes : list, sorting_algorithm : typing.Callable) -> None:
    """
    DESCRIPTION
    Times how long an algorithm takes to sort randomly generated lists of specified sizes
    Results are printed to the console

    PARAMETERS
    list_sizes: A list of N values used to generate a random list of numbers to sort
    sorting_algorithm: The function that will be used to sort the generated list of numbers

    RETURN
    no return
    """
    runtimes = {size:[] for size in list_sizes}
    for i in range(1, SAMPLE_SIZE + 1): # Add 1 because range is exclusive, and we want to start at 1
        print("Running Algorithm, Iteration [" + str(i) + "/" + str(SAMPLE_SIZE) + "]")
        for list_size in list_sizes:
            # Generate list to sort
            list_of_values = generate_random_values(list_size)
            # Time Algorithm
            start_time = time.perf_counter()
            sorting_algorithm(list_of_values)
            end_time = time.perf_counter()
            time_elapsed = (end_time - start_time)
            # Add Runtime to Data
            print("Sorted: N = " + str(list_size) + ", T = " + str(time_elapsed))
            runtimes[list_size].append(time_elapsed)

    # Presentation
    print("=== AVERAGE TIMES ===")
    for list_size in list_sizes:
        average = statistics.mean(runtimes[list_size])
        print(str(list_size) + " : " + str(average))