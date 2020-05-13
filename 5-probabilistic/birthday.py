import matplotlib.pyplot as plt


def probabilistic_solution(y):
    q = 1  # probability no pair
    i = 0  # the number of people
    p = 0.5
    while q > 1-p:
        i += 1
        q *= (y-i+1)/y
    return i


def probabilistic_solution_test():
    Y = 365
    print(f"Y = {Y}")
    print(f"probabilistic anser = {probabilistic_solution(Y)}")


def indicator_solution(y):
    left = 1
    right = y  # y is large enough.
    e = 1
    while left+1 != right and left != right:
        mid = (left+right) // 2
        mid_v = mid*(mid-1)/(2*y)
        if mid_v < e:
            left = mid
        else:
            right = mid
    left_d = abs(left*(left-1)/(2*y) - 1)
    right_d = abs(right*(right-1)/(2*y) - 1)
    if left_d < right_d:
        return left
    return right


def indicator_solution_test():
    Y = 365
    # Y = 669
    print(f"Y = {Y}")
    print(f"indicator answer = {indicator_solution(Y)}")


def graph():
    Y = [i for i in range(1, 3650)]
    np = [probabilistic_solution(y) for y in Y]  # answer of probabilistic
    ni = [indicator_solution(y) for y in Y]  # answer of indicator solution
    plt.plot(Y, np, label="probabilistic")
    plt.plot(Y, ni, label="indicator")
    plt.ylabel("n")
    plt.xlabel("Y")
    plt.legend()
    plt.show()
    # plt.savefig("com-p-i")


if __name__ == '__main__':
    probabilistic_solution_test()
    indicator_solution_test()
    graph()
