import copy
import numpy as np
from itertools import combinations


class Node:

    def __init__(self, k):
        self.key = k
        self.parent = None
        self.left = None
        self.right = None


def insert(root, n):
    # n is new node
    # return root
    y = None
    x = root
    while x is not None:
        y = x
        if n.key < x.key:
            x = x.left
        else:
            x = x.right
    n.parent = y
    if y is None:
        return n  # root is None
    elif n.key < y.key:
        y.left = n
    else:
        y.right = n
    return root


def gen_tree(numbers):
    root = None
    for n in numbers:
        root = insert(root, Node(n))
    return root


answer1 = []  # save the answer of solution1


def solution1(numbers):
    # ルートから、選択できるノードを順番に選択する
    # 選択されたノードの子ノードを選択肢に追加する

    # building a tree
    root = gen_tree(numbers)
    choices = [root]
    record = []
    choose(choices, record, None)


def choose(choices, record, chosen):
    if chosen is not None:
        # print(f'{chosen.key} is selected.')
        record.append(chosen.key)
        if chosen.right is not None:
            choices.append(chosen.right)
        if chosen.left is not None:
            choices.append(chosen.left)

    for choice in choices:
        choose([c for c in choices if c is not choice], copy.deepcopy(record), choice)
    if len(choices) == 0:
        answer1.append(record)


def solution2(numbers):
    # solve recursively

    # building a tree
    root = gen_tree(numbers)
    answer = solve2(root)
    return answer


def solve2(root):
    # return the answer of the partial tree
    if root is None:
        return []
    l_arrays = solve2(root.left)
    r_arrays = solve2(root.right)
    if len(l_arrays) == 0 and len(r_arrays) == 0:
        return [[root.key]]
    if len(l_arrays) == 0:
        for arr in r_arrays:
            arr.insert(0, root.key)
        return r_arrays
    if len(r_arrays) == 0:
        for arr in l_arrays:
            arr.insert(0, root.key)
        return l_arrays

    # combine both r and l answers. the first element is this node
    answers = []
    for l_array in l_arrays:
        for r_array in r_arrays:
            answers.extend(combine_arrays(l_array, r_array, root.key))
    return answers


# def combine_arrays(l_array, l_index, r_array, r_index, current, answers):
def combine_arrays(a, b, r):
    result = []
    n = len(a) + len(b)
    for indA in combinations(range(n), len(a)):
        x = np.zeros(n, dtype=int)
        mask = np.zeros(n, dtype=bool)
        mask[indA,] = True    # The ',' is important here for indexing
        x[mask] = a
        x[~mask] = b
        x = list(x)
        x.insert(0, r)
        result.append(x)
    return result


if __name__ == '__main__':
    # input_numbers = [4, 2, 1, 3, 5]
    input_numbers = [4, 2, 1, 3, 6, 5, 7]
    solution1(input_numbers)
    print(answer1)
    print(len(answer1))
    ans2 = solution2(input_numbers)
    print(ans2)
    print(len(ans2))
    if len(answer1) != len(ans2):
        print("incorrect")
    for a1 in answer1:
        if a1 not in ans2:
            print("incorrect")
