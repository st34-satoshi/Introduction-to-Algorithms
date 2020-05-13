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


def hire_assistant_test():
    # prepare data
    N = 30  # size of candidates
    candidates = [random.randint(1, N**3) for _ in range(N)]
    print(f"candidates: {candidates}")
    count, h = hire_assistant(candidates)
    print(f"hire count = {count}")
    print(f"hire = {h}, ability = {candidates[h]}")
    print(f"max ability in candidates = {max(candidates)}")


def hire_mean_count():
    # TODO:
    # mean count of hiring
    E = 100  # number of experiments
    N = 30  # size of candidates


if __name__ == '__main__':
    hire_assistant_test()
