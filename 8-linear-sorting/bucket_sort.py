import random
import copy


def insert_sort(numbers):
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]


def bucket_sort(numbers):
    # the elements are [0, 1)
    s = len(numbers)
    b = [[] for _ in range(s)]
    for n in numbers:
        b[int(s*n)].append(n)
    for i in range(len(b)):
        insert_sort(b[i])
    ans = []
    for bl in b:
        ans.extend(bl)
    return ans


def square_each_bucket(size):
    numbers = [random.random() for _ in range(size)]
    b = [[] for _ in range(size)]
    for n in numbers:
        b[int(size*n)].append(n)
    squ = 0
    for bl in b:
        squ += len(bl)**2
    squ /= size
    return squ


def experiment():
    # check the E[n_i^2] = 2 - 1/n
    print("E[n_i^2] = 2 - 1/n experiment")
    e = 100  # the number of experiment
    size = 100  # the number of list size
    ave = 0
    for _ in range(e):
        ave += square_each_bucket(size)
    ave /= e
    print(f'n = {size}')
    print(f'2 - 1/n = {2-1/size}')
    print(f'experiment = {ave}')


if __name__ == '__main__':
    numb = [random.random() for _ in range(20)]
    print(numb)
    ins = copy.deepcopy(numb)
    insert_sort(ins)
    print(ins)
    print(bucket_sort(copy.deepcopy(numb)))
    experiment()
