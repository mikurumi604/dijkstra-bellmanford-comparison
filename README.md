# Dijkstra vs Bellman-Ford

A small experimental project comparing the runtime and behavior
of Dijkstra's algorithm and the Bellman-Ford algorithm.

## Objectives

- Implement Dijkstra and Bellman-Ford from scratch
- Compare their execution time on randomly generated graphs
- Investigate how the number of vertices and edges affects runtime
- Test the behavior of the algorithms with negative-weight edges
- Implement negative-cycle detection for Bellman-Ford

## Algorithms

- Dijkstra
- Bellman-Ford

### Dijkstra

- Approach: Greedy strategy that selects the unvisited node with the minimum tentative distance.
- Time Complexity: O(V^2 + E) using array lookup.
- Constraint: Requires all edge weights to be non-negative.

### Bellman-Ford

- Approach: Dynamic programming / edge relaxation over $V - 1$ passes.
- Time Complexity: O(VE), which becomes O(V^3) on dense graphs where E = THETA(V^2).
- Feature: Handles negative-weight edges and detects reachable negative cycles via an extra relaxation round.

## Experimental Setup

- Graph Model: Random directed graphs generated with edge probability $p$, plus guaranteed backbone edges between consecutive vertices.
- Timing: 10 runs per configuration using time.perf_counter(), reporting average execution time.
- Tests:
    Scaling Vertices (V):  V in [50, 250] with fixed p = 0.5.
    Scaling Edges (E): Fixed V = 100 with p in [0.01, 0.99].

## Results

- V Scaling (p = 0.5):
    Bellman-Ford is significantly slower than Dijkstra, widening from 16.27x at V=50 to 102.54x at V=250.
    Matches the theoretical gap of O(V^2) vs O(V^3) on dense graphs.
- E Scaling (V = 100):
    Bellman-Ford runtime scales linearly with edge additions (from 0.00194s to 0.05894s).
    Dijkstra's runtime remains dominated by vertex selection O(V^2), making it far less sensitive to edge density.

## Negative-weight Edge Test

- Tested on the counterexample in main2.py:
    Graph: A -> B (1), A -> C (2), B -> D (1), C -> B (-3).
    Dijkstra: Fails. Greedily finalizes B with distance 1, missing the shorter route A -> C -> B (-1) and yielding d(D) = 2.Bellman-Ford: Succeeds. Multiple relaxation rounds correctly find A -> C -> B -> D with distance 0.Negative Cycles: Bellman-Ford successfully returns 'negative cycle' if a reachable cycle with negative total weight exists.

## Conclusion

- Dijkstra is much faster for standard graphs with non-negative weights.
- Bellman-Ford is computationally heavier (O(VE)), but is essential when handling graphs with negative weights or    when detecting negative cycles.