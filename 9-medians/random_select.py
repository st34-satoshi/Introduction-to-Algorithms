import random
import time
import matplotlib.pyplot as plt


def partition(numbers, p, r):
    x = numbers[r]
    i = p - 1
    for j in range(p, r):
        if numbers[j] < x:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[r] = numbers[r], numbers[i+1]
    return i + 1


def random_partition(numbers, p, r):
    i = random.randint(p, r)
    numbers[i], numbers[r] = numbers[r], numbers[i]
    return partition(numbers, p, r)


def random_select(numbers, p, r, i):
    if p == r:
        return numbers[p]
    q = random_partition(numbers, p, r)
    k = q - p + 1
    if i == k:
        return numbers[q]
    elif i < k:
        return random_select(numbers, p, q-1, i)
    return random_select(numbers, q+1, r, i-k)


def measure_time(size, times):
    total_time = 0
    for _ in range(times):
        A = [random.randint(0, 10000) for _ in range(size)]
        select_i = random.randint(1, size)
        start_time = time.time()
        _ = random_select(A, 0, size-1, select_i)
        total_time += time.time() - start_time
    return total_time / times  # average time


def compare_time():
    exp_times = 100
    # sizes = [(s+1)*5000 for s in range(10)]  # you can change the size set of arrays for experiment
    sizes = [(s+1)*5 for s in range(100)]
    average_time = [measure_time(s, exp_times) for s in sizes]
    print(average_time)
    # graph
    plt.plot(sizes, average_time)
    plt.ylabel("computing time")
    plt.xlabel("the size of number array")
    # plt.show()
    plt.savefig("random_select_time1")


if __name__ == '__main__':
    compare_time()
