import copy


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


if __name__ == '__main__':
    # input_numbers = [4, 2, 1, 3, 5]
    input_numbers = [4, 2, 1, 3, 6, 5, 7]
    solution1(input_numbers)
    print(answer1)
    print(len(answer1))
