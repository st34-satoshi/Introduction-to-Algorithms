import random


def gen_list(n):
    li = [i+1 for i in range(n)]
    random.shuffle(li)
    return li


def left_right(i):
    # return children index
    left = (i+1) * 2 - 1
    right = (i+1) * 2 + 1 - 1
    return left, right


def max_heapify(numbers, i):
    l, r = left_right(i)
    size = len(numbers)
    largest = i
    if l < size and numbers[l] > numbers[largest]:
        largest = l
    if r < size and numbers[r] > numbers[largest]:
        largest = r
    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]
        max_heapify(numbers, largest)


def build_max_heap(numbers):
    size = len(numbers)
    for i in reversed(range(0, size//2)):
        max_heapify(numbers, i)


def heap_sort(inp):
    numbers = [n for n in inp]
    build_max_heap(numbers)
    size = len(numbers)
    for i in reversed(range(1, size)):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        inp[i] = numbers.pop(-1)
        max_heapify(numbers, 0)
    inp[0] = numbers[0]


if __name__ == '__main__':
    N = 10
    A = gen_list(N)
    print("before ")
    print(A)
    build_max_heap(A)
    print("built max heap")
    print(A)
    heap_sort(A)
    print("sorted")
    print(A)
