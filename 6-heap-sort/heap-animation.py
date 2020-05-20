import random
from gvanim import Animation, render, gif
from graphviz import Graph


def gen_list(n):
    li = [i+1 for i in range(n)]
    random.shuffle(li)
    return li


def left_right(i):
    # return children index
    left = (i+1) * 2 - 1
    right = (i+1) * 2 + 1 - 1
    return left, right


def max_heapify(numbers, i, ga=None):
    l, r = left_right(i)
    size = len(numbers)
    largest = i
    if l < size and numbers[l] > numbers[largest]:
        largest = l
    if r < size and numbers[r] > numbers[largest]:
        largest = r
    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]
        if ga is not None:
            ga.highlight_node(i+1)
            ga.highlight_node(largest+1)
            ga.next_step()
            ga.label_node(i+1, numbers[i])
            ga.label_node(largest+1, numbers[largest])
            ga.next_step()
        max_heapify(numbers, largest, ga)


def build_max_heap(numbers):
    size = len(numbers)

    ga = Animation()
    # add nodes and edges
    for i in reversed(range(size)):
        v = numbers[i]
        ga.label_node(i+1, v)
        if i != 0:
            ga.add_edge((i+1)//2, i+1)
    ga.next_step()

    for i in reversed(range(0, size//2)):
        max_heapify(numbers, i, ga)

    # save
    graphs = ga.graphs()
    files = render(graphs, "figure/fig", 'png')
    gif(files, "figure/building-heap", 50)


def heap_sort(inp):
    numbers = [n for n in inp]
    build_max_heap(numbers)
    size = len(numbers)
    for i in reversed(range(1, size)):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        inp[i] = numbers.pop(-1)
        max_heapify(numbers, 0)
    inp[0] = numbers[0]


def draw_graph(numbers, name):
    dot = Graph(comment=name, format="png")
    size = len(numbers)
    # add node
    for i, v in enumerate(numbers):
        n = i + 1
        dot.node(str(n), str(v))
    # add edge
    for i, v in enumerate(numbers):
        n = i + 1
        # add children edge
        if n * 2 <= size:
            dot.edge(str(n), str(2*n))
        if n * 2 + 1 <= size:
            dot.edge(str(n), str(2*n+1))

    # save
    dot.render()


if __name__ == '__main__':
    N = 10
    A = gen_list(N)
    print("before ")
    print(A)
    heap_sort(A)
    print("sorted")
    print(A)
    draw_graph(A, "a")
