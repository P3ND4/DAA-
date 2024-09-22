try:
    from utils.heap import MinHeap
except:
    from heap import MinHeap
import math
def Dijkstra(adj: list[list[tuple[int, int]]]):
    d = [math.inf]*len(adj)
    d[0] = 0
    visited = [False]*len(adj)
    min_heap = MinHeap()
    min_heap.insert(0, d[0])
    while(len(min_heap)):
        node, weight, ad = min_heap.extract_min()
        if visited[node]: continue
        visited[node] = True
        for nod, edge_weight in adj[node]:
            min_heap.insert(nod, d[node] + edge_weight, node)
            relax(nod, edge_weight, node, d)
    
    return d
    



def relax(vertex: int, edge_weight: int, adjacent: int, d: list[int]):
    d[vertex] = min(edge_weight+ d[adjacent], d[vertex])




adj = [
    [(1,25), (5, 5)],
    [(0, 25), (8, 5)],
    [(5, 10), (8, 10), (3, 3), (4,10)],
    [(2, 3), (4,27)],
    [(2,10), (3,27)],
    [(0,5),(2, 10),(6, 30)],
    [(5, 30), (7, 1)],
    [(6, 1)],
    [(1, 5), (2, 10)]
    ]
print(Dijkstra(adj))