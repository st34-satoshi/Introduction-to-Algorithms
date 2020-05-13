import random


def hire_assistant(n):
    best = 0
    hire = None
    cnt = 0
    for i in range(len(n)):
        if n[i] > best:
            best = n[i]
            cnt += 1
            hire = i
    return cnt, hire


def hire_assistant_random(n):
    random.shuffle(n)
    best = 0
    hire = None
    cnt = 0
    for i in range(len(n)):
        if n[i] > best:
            best = n[i]
            cnt += 1
            hire = i
    return cnt, hire


def hire_assistant_test():
    # prepare data
    N = 30  # size of candidates
    candidates = [random.randint(1, N**3) for _ in range(N)]
    print(f"candidates: {candidates}")
    count, h = hire_assistant(candidates)
    print(f"hire count = {count}")
    print(f"hire = {h}, ability = {candidates[h]}")
    print(f"max ability in candidates = {max(candidates)}")


def average_number_hiring(candidates):
    ans = 0
    for i in range(1, len(candidates)+1):
        ans += 1 / i
    return ans


def hire_experiment():
    # mean count of hiring
    E = 1000  # number of experiments
    N = 30  # size of candidates
    total_hiring_cnt = 0
    for _ in range(E):
        # prepare data
        candidates = [random.randint(1, N**3) for _ in range(N)]
        count, _ = hire_assistant(candidates)
        total_hiring_cnt += count
    print(f"number of experiments = {E}")
    print(f"size of candidates = {N}")
    print(f"mean of the number of hiring = {total_hiring_cnt/E}")
    average_hiring = average_number_hiring(candidates)
    print(f"computed average hiring number = {average_hiring}")


if __name__ == '__main__':
    # hire_assistant_test()
    hire_experiment()
