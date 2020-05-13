import random
import math


def random_ab(a, b):
    # I can use random(0, 1)
    diff = b - a
    bit_n = int(math.log2(diff)) + 1
    while True:  # until find answer
        # create answer
        ans = 0
        for i in range(bit_n):
            r = random.randint(0, 1)
            ans += r * 2**i
        if diff >= ans:
            return a + ans


def random_ab_test():
    a = 3
    b = 8
    E = 10000
    record = [0]*10
    for _ in range(E):
        r = random_ab(a, b)
        record[r] += 1
    print(record)


def random_p(p):
    r = random.random()
    if r < p:
        return 1
    return 0


def random_01(p):
    while True:
        r1 = random_p(p)
        r2 = random_p(p)
        if r1 == 0 and r2 == 1:
            return 1
        if r1 == 1 and r2 == 0:
            return 0


def random_01_test():
    E = 10000
    record = [0]*3
    p = random.random()
    for _ in range(E):
        r = random_01(p)
        record[r] += 1
    print(record)


if __name__ == '__main__':
    random_ab_test()
    random_01_test()

