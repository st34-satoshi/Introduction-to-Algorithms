import random


def minimum(numbers):
    mini = numbers[0]
    for i in range(1, len(numbers)):
        if mini > numbers[i]:
            mini = numbers[i]
    return mini


def gen_numbers(size):
    return [random.randint(1, 100) for _ in range(size)]


def min_and_max(numbers):
    even = len(numbers) % 2 == 0
    mini = numbers[0]
    maxi = numbers[0]
    start_i = 1
    if even:
        mini = min(numbers[0], numbers[1])
        maxi = max(numbers[0], numbers[1])
        start_i = 2
    for i in range((len(numbers)+1)//2):
        cmp1 = numbers[i+start_i]
        cmp2 = numbers[-(i+1)]
        if cmp1 < cmp2:
            if cmp1 < mini:
                mini = cmp1
            if cmp2 > maxi:
                maxi = cmp2
        else:
            if cmp2 < mini:
                mini = cmp2
            if cmp1 > maxi:
                maxi = cmp1
    return mini, maxi


if __name__ == '__main__':
    A = gen_numbers(10)
    print(f'numbers = {A}')
    print(f'min = {minimum(A)}')
    print(f'min and max = {min_and_max(A)}')
