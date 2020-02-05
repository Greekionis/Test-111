import networkx as nx


def main(G, src, dst, visited):
    c_c = 1                     # Компонент связности. Раз зашли, значит точно уже 1 есть.
    if src in visited and dst in visited:   # dst и src должны принадлежать visited
        for i in visited:           # Проход по нодам
            if not visited[i] and i < dst:      # Если ноду еще не посещали и следующая нода старше предыдущей
                if not walk(G, i, dst, visited):        # Идем от первой непосещенной ноды из списка нод до dst
                    c_c += 1                              # Увеличиваем КС, получая False от walk().
        return c_c
    else:
        return "Неверные вершины"


def walk(G, src, dst, visited):
    visited[src] = True
    if src == dst:
        return True
    for node in G.adj[src]:
        if not visited[node]:
            if walk(G, node, dst, visited):
                return True
    return False


if __name__ == "__main__":
    G = nx.Graph()
    g_lst = "ABCDEFG"
    #src = g_lst[0]
    #dst = g_lst[-1:]
    src = "A"
    dst = "G"

    G.add_nodes_from(g_lst)
    G.add_edges_from(
        [
            ("A", "B"),
            ("B", "C"),
            ("C", "D"),
            ("F", "G"),
        ]
    )
    visited = {node: False for node in G.nodes}

    print(main(G, src, dst, visited))
