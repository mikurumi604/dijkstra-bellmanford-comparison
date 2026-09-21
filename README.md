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

### Dijkstra

- Approach: Greedy strategy that selects the unvisited vertex with the minimum tentative distance.
- Time Complexity: O(V² + E) using linear search for the minimum-distance vertex.
- Constraint: Requires all edge weights to be non-negative.

### Bellman-Ford

- Approach: Repeatedly relaxes all edges for V - 1 passes.
- Time Complexity: O(VE), which becomes O(V³) on dense graphs where E = Θ(V²).
- Feature: Handles negative-weight edges and detects reachable negative cycles via an extra relaxation round.

## Experimental Setup

- Graph Model: Random directed graphs generated with edge probability p, plus guaranteed backbone edges between consecutive vertices.
- Timing: 10 runs per configuration using `time.perf_counter()`, reporting average execution time.
- Tests:
  - Scaling Vertices (V): V in [50, 250] with fixed p = 0.5.
  - Scaling Edges (E): Fixed V = 100 with p in [0.01, 0.99].

## Results

### V Scaling (p = 0.5)

Bellman-Ford was substantially slower than Dijkstra, with the measured ratio increasing from 16.27x at V = 50 to 102.54x at V = 250.

This is consistent with the theoretical complexity gap of O(V²) for Dijkstra and O(V³) for Bellman-Ford on the dense graphs used in this experiment.

### E Scaling (V = 100)

Bellman-Ford's measured runtime generally increased as the number of edges increased, from 0.00194s to 0.05894s.

With V fixed, the O(VE) complexity of Bellman-Ford implies that its dominant operation count grows linearly with E.

Dijkstra was less sensitive to edge density in this experiment because its O(V²) vertex-selection cost remained a major part of its runtime.

## Negative-weight Edge Test

A counterexample was tested in `main2.py`:

```text
A -> B (1)
A -> C (2)
B -> D (1)
C -> B (-3)
```

Dijkstra: Fails. It finalizes B with distance 1 before discovering the shorter route A -> C -> B with distance -1, leaving d(D) = 2.

Bellman-Ford: Succeeds. Repeated relaxation finds A -> C -> B -> D with total distance 0.

Negative Cycles: Bellman-Ford returns negative cycle when a reachable negative cycle is detected.

## Conclusion

In the experiments, Dijkstra was substantially faster on the tested graphs with non-negative edge weights.
Bellman-Ford is computationally heavier with O(VE) time complexity, but it can handle negative-weight edges and detect reachable negative cycles.