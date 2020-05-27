import random


def gen_numbers(size, max_number):
    numbers = [random.randint(0, max_number) for _ in range(size)]
    return numbers


def counting_sort(numbers, max_number):
    c = [0]*(max_number+1)
    # count the number
    for n in numbers:
        c[n] += 1
    # count the cumulative sum
    for i in range(1, len(c)):
        c[i] += c[i-1]
    print(c)
    ans = [0]*len(numbers)
    for i in reversed(range(len(numbers))):
        ans[c[numbers[i]]-1] = numbers[i]
        c[numbers[i]] -= 1
    return ans


if __name__ == '__main__':
    MAX = 10
    SIZE = 10
    a = gen_numbers(SIZE, MAX)
    print(a)
    sorted_a = counting_sort(a, MAX)
    print(sorted_a)
