import algo_timer
import algorithms

# CONSTANT - List sizes of N to test the sorting algorithm on
LIST_SIZES = [
    5000,
    7500,
    10000,
    12500,
    15000,
    17500,
    20000,
    22500,
    25000
]

def calculate_insertion_sort_average_time() -> None:
    """
    DESCRIPTION
    Calculates average insert sort time for a list of sizes
    Results are printed to console

    PARAMETERS
    none

    RETURN
    no return
    """
    # Get Average Runtimes
    algorithm = algorithms.insertion_sort
    algo_timer.time_algorithm(LIST_SIZES, algorithm)

if __name__ == "__main__":
    calculate_insertion_sort_average_time()
