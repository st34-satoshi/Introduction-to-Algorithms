import heapq
from graphviz import Graph


# Node of huffman tree
class Letter:

    def __init__(self, num, c, left=None, right=None):
        self.number = num
        self.c = c  # sometimes combination of letters
        self.left = left  # left is smaller than right
        self.right = right
        self.code = ''  # added after creating tree

    def __lt__(self, other):
        return self.number < other.number

    def __str__(self):
        return f'{self.c}({self.number}) code = {self.code}'
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
            return str(self.number)
        return self.c+''+str(self.number)

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


def solve(letters):
    # create tree
    while len(letters) >= 2:
        x = heapq.heappop(letters)
        y = heapq.heappop(letters)
        le = Letter(x.number+y.number, x.c+y.c, x, y)
        heapq.heappush(letters, le)
    root = letters[0]
    # decide the code
    root.set_code('')
    return root


if __name__ == '__main__':
    a = [('a', 45), ('b', 13), ('c', 12), ('d', 16), ('e', 9), ('f', 5)]
    a = [Letter(l[1], l[0]) for l in a]
    heapq.heapify(a)
    ans = solve(a)  # ans is the root of huffman tree
    ans.print()
    # make a graph
    graph = Graph(comment="Huffman tree", format="png")
    ans.graph(graph, None, None)

