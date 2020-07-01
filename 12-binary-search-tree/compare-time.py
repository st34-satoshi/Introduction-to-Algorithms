import time
import matplotlib.pyplot as plt
from binary_search_tree import gen_numbers, gen_tree


def gen_ordered_numbers(size):
    return list(range(size))


def compare_time():
    # compare time creating trees ordered and random
    sizes = [(i+1)*10 for i in range(10)]
    ex = 1000
    ordered_time = []
    random_time = []
    for size in sizes:
        print(f'size = {size}')
        total_order_time = 0
        for _ in range(ex):
            numbers = gen_ordered_numbers(size)
            start = time.time()
            gen_tree(numbers)
            total_order_time += time.time() - start
        ordered_time.append(total_order_time / ex)

        total_random_time = 0
        for _ in range(ex):
            numbers = gen_numbers(size)
            start = time.time()
            gen_tree(numbers)
            total_random_time += time.time() - start
        random_time.append(total_random_time / ex)
    print(ordered_time)
    print(random_time)
    plt.plot(sizes, ordered_time, label="ordered")
    plt.plot(sizes, random_time, label="random")
    plt.ylabel('time for creating tree')
    plt.xlabel('size of tree')
    plt.legend()
    # plt.show()
    plt.savefig("fig")

if __name__ == '__main__':
    compare_time()
