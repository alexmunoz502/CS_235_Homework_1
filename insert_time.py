import sys
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

DEFAULT_SAMPLE_SIZE = 3

def calculate_insertion_sort_average_time(sample_size: int) -> None:
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
    algo_timer.time_algorithm(LIST_SIZES, sample_size, algorithm)

if __name__ == "__main__":
    sample_size = DEFAULT_SAMPLE_SIZE
    if (len(sys.argv) > 1):
        try:
            # Parse input for custom sample size
            sample_size = int(sys.argv[1])
            calculate_insertion_sort_average_time(sample_size)
        except (ValueError):
            print("Invalid sample size. Please use a valid integer or "\
                f"run as default ({DEFAULT_SAMPLE_SIZE}).")
    else:
        calculate_insertion_sort_average_time(sample_size)
