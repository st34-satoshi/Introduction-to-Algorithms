# construct maximum binary tree
# install GraphvizAnim: `pip install GraphvizAnim`.  unfortunately, windows may have some trouble
from gvanim import Animation, render, gif
import os


class Node:

    def __init__(self, num):
        self.number = num
        self.left = None
        self.right = None

    def add_node(self, node):
        # return the root
        if self.number < node.number:
            node.left = self
            return node

        if self.right is None:
            self.right = node
            return self
        self.right = self.right.add_node(node)
        return self

    def print(self):
        print(f'this number = {self.number}')
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()

    def set_animation(self, ga):
        ga.add_node(self.number)
        if self.left is not None:
            ga.add_edge(self.number, self.left.number)
            self.left.set_animation(ga)
        if self.right is not None:
            ga.add_edge(self.number, self.right.number)
            self.right.set_animation(ga)


def construct(numbers):
    ga = Animation()  # for visualization
    root = Node(numbers[0])
    for n in numbers[1:]:
        root = root.add_node(Node(n))
        # each time rewrite all nodes. this is not good
        root.set_animation(ga)
        ga.next_step(clean=True)

    # print the result
    root.print()

    # save the animation
    if not os.path.isdir("graphs"):
        os.mkdir("graphs")
    graphs = ga.graphs()
    files = render(graphs, "graphs/figure", 'png')
    gif(files, "graphs/gif-anim", 50)


if __name__ == '__main__':
    _numbers = [5, 14, 12, 15, 16, 18, 6, 7, 1, 19, 4, 11, 0, 9, 3, 8, 2, 17, 10, 13]
    construct(_numbers)
