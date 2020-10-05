import algo_timer
import algorithms

#  CONSTANT - List sizes of N to test the sorting algorithm on
list_sizes = [
    500000,
    750000,
    1000000,
    1250000,
    1500000,
    1750000,
    2000000,
    2250000,
    2500000
]

def calculate_merge_sort_average_time() -> None:
    """
    DESCRIPTION
    Calculates average merge sort time for a list of sizes
    results are printed to console

    PARAMETERS
    none

    RETURN
    no return
    """
    # Get Average Runtimes
    algorithm = algorithms.merge_sort
    algo_timer.time_algorithm(list_sizes, algorithm)

if __name__ == "__main__":
    calculate_merge_sort_average_time()
