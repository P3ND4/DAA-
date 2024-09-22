from utils.heap import MinHeap
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