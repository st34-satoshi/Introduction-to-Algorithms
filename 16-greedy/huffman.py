import heapq
from graphviz import Graph


# Node of huffman tree
class Node:

    def __init__(self, num, letter, left=None, right=None):
        self.number = num
        self.letter = letter  # sometimes combination of letters. eg) a, b, c, ..., fe, fed, ...
        self.left = left  # left is smaller than right
        self.right = right
        self.code = ''  # added after creating tree

    def __lt__(self, other):
        return self.number < other.number

    def __str__(self):
        return f'{self.letter}({self.number}) code = {self.code}'
        # return f'number={self.number}, c={self.c}, code={self.code}'

    def set_code(self, previous):
        self.code = previous
        if self.left is not None:
            self.left.set_code(previous+'0')
        if self.right is not None:
            self.right.set_code(previous+'1')

    def print(self):
        if self.left is not None:  # and right is not None
            self.left.print()
            self.right.print()
        else:
            print(self)

    def node_name(self):
        if self.left is not None:  # and right is not None
            return self.letter+'('+str(self.number)+')'
        return self.letter+'('+str(self.number)+')'+','+self.code

    def graph(self, dot, parent, code):
        # code is 0 if left, code is 1 if right
        # add node
        dot.node(self.node_name())
        # add edge
        if parent is not None:
            dot.edge(parent.node_name(), self.node_name(), label=code)
        # add children
        if self.left is not None:  # and right is not None
            self.left.graph(dot, self, '0')
            self.right.graph(dot, self, '1')
        # root node saves the graph
        if parent is None:
            dot.render("huffman-graph")


def solve(nodes):
    # create tree
    while len(nodes) >= 2:  # n-1 times
        x = heapq.heappop(nodes)
        y = heapq.heappop(nodes)
        n = Node(x.number+y.number, x.letter+y.letter, x, y)
        heapq.heappush(nodes, n)
    root = nodes[0]
    # decide the code
    root.set_code('')
    return root


if __name__ == '__main__':
    # make a input
    a = [('a', 45), ('b', 13), ('c', 12), ('d', 16), ('e', 9), ('f', 5)]
    a = [Node(l[1], l[0]) for l in a]
    heapq.heapify(a)

    # solve
    ans = solve(a)  # ans is the root of huffman tree

    # print answer
    ans.print()
    # make a graph
    graph = Graph(comment="Huffman tree", format="png")
    ans.graph(graph, None, None)

