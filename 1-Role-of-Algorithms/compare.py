"""
    compare
"""
import insertion_sort
import merge_sort
import random
import copy
import time


def compare_merge_insert():
    N = 10**4  # change here to change array size. 10**4 is enough big, it takes about 5 seconds.
    arr_insert = [random.randint(0, 10**6) for _ in range(N)]
    arr_merge = copy.deepcopy(arr_insert)
    start_time = time.time()
    insertion_sort.insertionSort(arr_insert)
    insert_time = time.time() - start_time
    start_time = time.time()
    merge_sort.mergeSort(arr_merge)
    merge_time = time.time() - start_time

    # check error
    for i, n in enumerate(arr_insert):
        if n != arr_merge[i]:
            print("Error: result is not the same!, ", i)
            return
    print("result is the same")
    print("insert sort time = ", insert_time)
    print("merge  sort time = ", merge_time)


if __name__ == '__main__':
    compare_merge_insert()
