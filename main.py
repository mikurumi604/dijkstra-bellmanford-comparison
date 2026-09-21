#main.py
import time

from dijkstra import dijkstra
from bellmanford import bellmanford
from graph_generator import generate_graph, count_edges
from plot import plot_vertices, plot_edges

choice = input("vertex or edge: ")


if choice == 'vertex':

    nplot = []
    dplot = []
    bplot = []

    for n in [50, 100, 150, 200, 250]:

        graph = generate_graph(n, 0.5)
        dres, bres = [], []

        for _ in range(10):

            start = time.perf_counter()
            d = dijkstra(graph, 'v0')
            end = time.perf_counter()
            dres.append(end - start)

            start = time.perf_counter()
            b = bellmanford(graph, 'v0')
            end = time.perf_counter()
            bres.append(end - start)

        dave, bave = sum(dres) / len(dres), sum(bres) / len(bres)

        nplot.append(n)
        dplot.append(dave)
        bplot.append(bave)

        _, edge = count_edges(graph)

        print(f"n = {n}")
        print(f"dijkstra average : {dave}")
        print(f"bellmanford average : {bave}")
        print(f"ratio : {bave / dave}")
        print(f"edges : {edge}\n")

    plot_vertices(
        nplot,
        dplot,
        bplot
    )

elif choice == 'edge':

    eplot = []
    dplot = []
    bplot = []
    n = int(input("number of vertices: "))

    for p in [0.01, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99]:

        graph = generate_graph(n, p)
        dres, bres = [], []

        for _ in range(10):

            start = time.perf_counter()
            d = dijkstra(graph, 'v0')
            end = time.perf_counter()
            dres.append(end - start)

            start = time.perf_counter()
            b = bellmanford(graph, 'v0')
            end = time.perf_counter()
            bres.append(end - start)

        dave, bave = sum(dres) / len(dres), sum(bres) / len(bres)
        _, total = count_edges(graph)

        eplot.append(total)
        dplot.append(dave)
        bplot.append(bave)

        print(f"p = {p}, e = {total}")
        print(f"dijkstra average : {dave}")
        print(f"bellmanford average : {bave}")
        print(f"ratio : {bave / dave}\n")

    plot_edges(
        eplot,
        dplot,
        bplot
    )