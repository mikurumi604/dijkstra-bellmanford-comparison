#main2.py
import time
import random
from dijkstra import dijkstra
from bellmanford import bellmanford

graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('D', 1)],
    'C': [('B', -3)],
    'D': []
}

d = dijkstra(graph, 'A')
b = bellmanford(graph, 'A')

print(d)
print(b)
print('\n\n')

graph = {}
n = int(input())
edge_prob = float(input())

for i in range(n):

    graph[f'v{i}'] = []

    if i < n - 1:
        graph[f'v{i}'].append(
            (f'v{i+1}', random.randint(-50, 50))
        )

    for j in range(n):
        if i == j or i + 1 == j:
            continue
        if edge_prob > random.random():
            graph[f'v{i}'].append(
                (f'v{j}', random.randint(-50, 50))
            )

d = dijkstra(graph, 'v0')
b = bellmanford(graph, 'v0')

print(d, '\n', b)