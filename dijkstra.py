#dijkstra.py
def dijkstra(graph, start):
    ans = {
        v: (float('inf'), None)
        for v in graph
    }

    visited = set()

    ans[start] = (0, None)

    while len(visited) != len(ans):
        v, vdistance = '', float('inf')

        for ver in ans:
            if ver not in visited and ans[ver][0] <= vdistance:
                v, vdistance = ver, ans[ver][0]

        if vdistance == float('inf'):
            break

        for neighbor, weight in graph[v]:
            nd = ans[v][0] + weight

            if nd < ans[neighbor][0]:
                ans[neighbor] = (nd, v)

        visited.add(v)

    return ans