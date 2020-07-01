from gvanim import Animation, render, gif
from binary_search_tree import gen_numbers, insert, Node, delete, search


def animation():
    size = 10
    numbers = gen_numbers(size)
    root = None
    ga = Animation()
    # generate tree
    for n in numbers:
        root = insert(root, Node(n))
        add_nodes(ga, root)
        ga.highlight_node(n)
        ga.next_step(clean=True)
    # delete
    for n in gen_numbers(size):
        add_nodes(ga, root)
        ga.highlight_node(n)
        ga.next_step(clean=True)
        root = delete(root, search(root, n))

    # save
    graphs = ga.graphs()
    files = render(graphs, "figure/figure", 'png')
    gif(files, "figure/gif-anim", 50)


def add_nodes(ga, root):
    ga.add_node(root.key)
    if root.parent is not None:
        ga.add_edge(root.parent.key, root.key)
    if root.left is not None:
        add_nodes(ga, root.left)
    if root.right is not None:
        add_nodes(ga, root.right)


if __name__ == '__main__':
    animation()
    pass
