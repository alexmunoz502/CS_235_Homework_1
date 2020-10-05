import statistics
import random
import algorithms
import time

# Random Number Range
RANDOM_INT_MIN = 0
RANDOM_INT_MAX = 10000

# Generate new seed to prevent the same numbers each time
random.seed()

# Runtimes
sample_size = 10 # how many times to run each size sorting to get an average time
runtimes = {
    500000 : [],
    750000 : [],
    1000000 : [],
    1250000 : [],
    1500000 : [],
    1750000 : [],
    2000000 : [],
    2250000 : [],
    2500000 : []
}

def generate_random_values(list_size : int) -> list:
    number_list = []
    for _ in range(list_size):
        number_list.append(random.randint(RANDOM_INT_MIN, RANDOM_INT_MAX))
    return number_list

for i in range(1, sample_size+1):
    print("Running Algorithm, iteration " + str(i) +" of " + str(sample_size))
    for list_size in runtimes.keys():
        list_of_values = generate_random_values(list_size)
        start_time = time.perf_counter()
        algorithms.merge_sort(list_of_values)
        end_time = time.perf_counter()
        time_elapsed = (end_time - start_time)
        print("MERGE SORT: Sorted list of " + str(list_size) + " values in " + str(time_elapsed) + " seconds.")
        runtimes[list_size].append(time_elapsed)

print("=== AVERAGE TIMES ===")
for key in runtimes.keys():
    average = statistics.mean(runtimes[key])
    print(str(key) + " : " + str(average))




