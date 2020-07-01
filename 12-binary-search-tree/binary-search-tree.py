import random


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


def gen_numbers(size):
    return random.sample(list(range(size)), size)


def gen_tree(numbers):
    root = None
    for n in numbers:
        root = insert(root, Node(n))
    return root


def inorder_tree_walk(root):
    if root is not None:
        inorder_tree_walk(root.left)
        print(root.key, end=' ')
        inorder_tree_walk(root.right)


def search(root, k):
    if root is None or k == root.key:
        return root
    if k < root.key:
        return search(root.left, k)
    return search(root.right, k)


def minimum(root):
    x = root
    while x.left is not None:
        x = x.left
    return x


def maximum(root):
    x = root
    while x.right is not None:
        x = x.right
    return x


def successor(n):
    if n.right is not None:
        return minimum(n.right)
    y = n.parent
    while y is not None and n is y.right:
        n = y
        y = y.parent
    return y


def predecessor(n):
    if n.left is not None:
        return maximum(n.left)
    y = n.parent
    while y is not None and n is y.left:
        n = y
        y = y.parent
    return y


def transplant(root, u, v):
    if u.parent is None:
        return v
    if u is u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v is not None:
        v.parent = u.parent
    return root


def delete(root, n):
    if n.left is None:
        root = transplant(root, n, n.right)
    elif n.right is None:
        root = transplant(root, n, n.left)
    else:
        y = minimum(n.right)
        if y.parent is not n:
            root = transplant(root, y, y.right)
            y.right = n.right
            y.right.parent = y
        root = transplant(root, n, y)
        y.left = n.left
        y.left.parent = y
    return root


def sample_gen_tree():
    s = 10
    numbers = gen_numbers(s)
    print(numbers)
    root = gen_tree(numbers)
    print(root.key)


def sample_print_sorted_keys():
    s = 10
    numbers = gen_numbers(s)
    print(numbers)
    root = gen_tree(numbers)
    inorder_tree_walk(root)


def sample_search():
    s = 10
    numbers = gen_numbers(s)
    print(numbers)
    root = gen_tree(numbers)
    print(search(root, 3))
    print(search(root, 11))


def sample_delete():
    s = 10
    numbers = gen_numbers(s)
    print(numbers)
    root = gen_tree(numbers)
    inorder_tree_walk(root)
    print()
    delete_numbers = gen_numbers(s)
    for n in delete_numbers:
        print(f'delete = {n}')
        node = search(root, n)
        root = delete(root, node)
        inorder_tree_walk(root)
        print()


if __name__ == '__main__':
    # sample_gen_tree()
    # sample_print_sorted_keys()
    # sample_search()
    sample_delete()
    pass
