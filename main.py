import random
import time

import quick
import merge
import shell
import heap
import quick_s


def make_random_array(num):
    a = []
    for i in range(num):
        a.append(random.randint(1, 100000))
    return a


def make_unrandom_array(num):
    return list(range(1, num))


def execute_the_program_random(num):
    array1 = make_random_array(num)

    array = array1.copy()
    start = time.time()
    quick.quick_sort(array, 0, len(array)-1)
    end = time.time()
    print("Quicksort, random,", num, ":", end - start)

    array = array1.copy()
    start = time.time()
    merge.merge_sort(array)
    end = time.time()
    print("Merge sort, random,", num, ":", end - start)

    array = array1.copy()
    start = time.time()
    shell.shellsort(array, len(array))
    end = time.time()
    print("Shellsort, random,", num, ":", end - start)

    array = array1.copy()
    start = time.time()
    heap.heapsort(array)
    end = time.time()
    print("Heapsort, random,", num, ":", end - start)


def execute_the_program_unrandom(num):
    array2 = make_unrandom_array(num)

    array = array2.copy()
    start = time.time()
    quick_s.iterative_quicksort(array)
    end = time.time()
    print("Quicksort, not random,", num, ":", end - start)

    array = array2.copy()
    start = time.time()
    merge.merge_sort(array)
    end = time.time()
    print("Merge sort, not random,", num, ":", end - start)

    array = array2.copy()
    start = time.time()
    shell.shellsort(array, len(array))
    end = time.time()
    print("Shellsort, not random,", num, ":", end - start)

    array = array2.copy()
    start = time.time()
    heap.heapsort(array)
    end = time.time()
    print("Heapsort, not random,", num, ":", end - start)


execute_the_program_random(100_000)
print()
# execute_the_program_random(250_000)
print()

execute_the_program_unrandom(100_000)
print()
# execute_the_program_unrandom(250_000)
print()