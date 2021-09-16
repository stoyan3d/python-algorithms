from random import randint
from timeit import repeat


def run_search_algorithm(algorithm, array, query):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from algorithms.search import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array}, {query})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


ARRAY_LENGTH = 100000

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    run_search_algorithm(algorithm="linear_search", array=array, query=256)
    run_search_algorithm(algorithm="binary_search", array=array, query=256)
