import random


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def random_partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)


def quick_sort(A, p, r):
    if p < r:
        # q = partition(A, p, r)  # use this if you do not want random
        q = random_partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def test():
    size = 10
    numbers = [random.randint(0, 10) for _ in range(size)]
    print(numbers)
    quick_sort(numbers, 0, size-1)
    print(numbers)


if __name__ == '__main__':
    test()
