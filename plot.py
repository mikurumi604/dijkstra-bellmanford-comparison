#plot.py
import matplotlib.pyplot as plt


def plot_vertices(n, dijkstra_time, bellmanford_time):

    plt.plot(n, dijkstra_time, marker='o', label='Dijkstra')
    plt.plot(n, bellmanford_time, marker='o', label='Bellman-Ford')

    plt.xlabel('Number of vertices (V)')
    plt.ylabel('Execution time (seconds)')
    plt.title('Execution Time vs Number of Vertices')

    plt.grid(True, which='both', linestyle='--', alpha=0.3)
    plt.yscale('log')
    plt.legend()
    plt.show()


def plot_edges(e, dijkstra_time, bellmanford_time):

    plt.plot(e, dijkstra_time, marker='o', label='Dijkstra')
    plt.plot(e, bellmanford_time, marker='o', label='Bellman-Ford')

    plt.xlabel('Number of edges (E)')
    plt.ylabel('Execution time (seconds)')
    plt.title('Execution Time vs Number of Edges')

    plt.grid(True, which='both', linestyle='--', alpha=0.3)
    plt.yscale('log')
    plt.legend()
    plt.show()