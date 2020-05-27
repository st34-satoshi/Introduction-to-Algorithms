import math
from counting_sort import gen_numbers


def gen_digit(number, base, d):
    return (number // (base**(d-1))) % base


def counting_sort_with_d(numbers, base, d):
    c = [0]*(base+1)
    # count the number
    for n in numbers:
        c[gen_digit(n, base, d)] += 1
    # count the cumulative sum
    for i in range(1, len(c)):
        c[i] += c[i-1]
    ans = [0]*len(numbers)
    for i in reversed(range(len(numbers))):
        ans[c[gen_digit(numbers[i], base, d)]-1] = numbers[i]
        c[gen_digit(numbers[i], base, d)] -= 1
    return ans


def radix_sort(numbers, max_number):
    base = 10
    max_d = int(math.log(max_number, base))
    for d in range(1, max_d+2):
        numbers = counting_sort_with_d(numbers, base, d)
    return numbers


if __name__ == '__main__':
    max_n = 20
    s = 10
    a = gen_numbers(s, max_n)
    print(a)
    answ = radix_sort(a, max_n)
    print(answ)

