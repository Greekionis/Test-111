import networkx as nx

orders = [
    (6, 8),
    (5, 7),
    (3, 9),
    (8, 10)
]


def plot():
    rocket = 0
    graph = nx.MultiDiGraph()
    graph.add_nodes_from(range(0, 23))
    for order in orders:
        for i in range(order[0], order[1]):
            graph.add_edge(i, i + 1)


    for d in graph.out_degree:
        if d[1] > rocket:
            rocket = d[1]
    return rocket


if __name__ == "__main__":
    print(plot())
