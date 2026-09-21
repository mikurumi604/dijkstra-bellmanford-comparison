#bellmanford.py
def bellmanford(graph, start):
    ans = {
        v: (float('inf'), None)
        for v in graph
    }

    n = len(graph)
    ans[start] = (0, None)

    for _ in range(n - 1):

        for v in graph:

            for neighbor, distance in graph[v]:

                nd = ans[v][0] + distance
                if nd < ans[neighbor][0]:
                    ans[neighbor] = (nd, v)

    for v in graph:
        for neighbor, distance in graph[v]:
        
            if ans[v][0] == float('inf'):
                continue
            
            nd = ans[v][0] + distance
    
            if nd < ans[neighbor][0]:
                return 'negative cycle'

    return ans

