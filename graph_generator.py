#graph_generator.py
import random


def generate_graph(n, edge_prob):

    graph = {}
    for i in range(n):

        graph[f'v{i}'] = []
        if i < n - 1:
            graph[f'v{i}'].append(
                (f'v{i+1}', random.randint(1, 100))
            )

        for j in range(n):
            if i == j or i + 1 == j:
                continue

            if edge_prob > random.random():
                graph[f'v{i}'].append(
                    (f'v{j}', random.randint(1, 100))
                )

    return graph


def count_edges(graph):
    edges_nums = {}
    total = 0

    for i, j in graph.items():
        n = len(j)
        edges_nums[i] = n
        total += n

    return edges_nums, total


