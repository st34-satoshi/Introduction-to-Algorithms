from graphviz import Digraph
import random


class Node:

    def __init__(self, key, none_node=None, color='red'):
        self.key = key
        self.color = color  # initial color is red
        self.right = none_node
        self.left = none_node
        self.parent = None

    def set_right(self, n):
        self.right = n
        if n.key == 9 and self.key == 6:
            print("hoge")

    def set_left(self, n):
        self.left = n

    def child(self, right):
        # right is a bool
        if right:
            return self.right
        return self.left

    def is_none(self):
        return self.key == -1


NoneNode = Node(-1, color='black')


def graph(root, save_name):
    # make a graph of present tree
    dot = Digraph(comment='red-black-tree', format="png")
    graph_walk(root, dot)
    dot.render(save_name)  # save as png file


def graph_walk(root, dot):
    # tree walk for making a graph
    if root is not None and not root.is_none():
        dot.node(str(root.key), color=root.color)
        if root.parent is not None:
            dot.edge(str(root.parent.key), str(root.key))
        graph_walk(root.right, dot)
        graph_walk(root.left, dot)


def left_rotate(root, x):
    y = x.right
    x.set_right(y.left)
    if not y.left.is_none():
        y.left.parent = x
    y.parent = x.parent
    if x.parent is None:
        root = y
    elif x is x.parent.left:
        x.parent.set_left(y)
    else:
        x.parent.set_right(y)
    y.set_left(x)
    x.parent = y
    return root


def right_rotate(root, x):
    y = x.left
    x.set_left(y.right)
    if not y.right.is_none():
        y.right.parent = x
    y.parent = x.parent
    if x.parent is None:
        root = y
    elif x is x.parent.left:
        x.parent.set_left(y)
    else:
        x.parent.set_right(y)
    y.set_right(x)
    x.parent = y
    return root


def rb_insert_fixup(root, z):
    # z is a new node. the color is red at first
    while z.parent is not None and z.parent.color == 'red':
        if z.parent is z.parent.parent.left:
            root, z = rb_insert_fixup_recover(root, z, True)
        else:
            root, z = rb_insert_fixup_recover(root, z, False)
    root.color = 'black'
    return root


def rb_insert_fixup_recover(root, z, right):
    y = z.parent.parent.child(right)
    if y.color == 'red':
        z.parent.color = 'black'
        y.color = 'black'
        z.parent.parent.color = 'red'
        z = z.parent.parent
    else:
        if z is z.parent.child(right):
            z = z.parent
            root = left_rotate(root, z) if right else right_rotate(root, z)
        z.parent.color = 'black'
        z.parent.parent.color = 'red'
        root = right_rotate(root, z.parent.parent) if right else left_rotate(root, z.parent.parent)
    return root, z


def rb_insert(root, z):
    x = root
    y = None
    while x is not None and not x.is_none():
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y is None:
        root = z
        root.color = 'black'
        return root
    elif z.key < y.key:
        y.set_left(z)
    else:
        y.set_right(z)
    root = rb_insert_fixup(root, z)
    return root


def gen_numbers(size):
    return random.sample(list(range(size)), size)


def insert_test():
    # NoneNode = Node(-1, color='black')
    # numbers = gen_numbers(10)
    numbers = [5, 2, 6, 8, 0, 9, 1, 3, 4, 7]
    root = None
    for i, n in enumerate(numbers):
        root = rb_insert(root, Node(n, none_node=NoneNode))
        graph(root, 'graph/create'+str(i))


if __name__ == '__main__':
    # a = Node(1)
    # b = Node(2)
    # b.parent = a
    # a.right = b
    # graph(a)
    # for _ in range(10):
    insert_test()
