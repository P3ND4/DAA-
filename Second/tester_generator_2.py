import random as rnd
import math




def genrate_conected_graph(max_len, max_w):
    v_count = rnd.randint(2, max_len)
    adj:list[list[int]] = []
    for i in range(0, v_count):
        adj.append([])
    visited = [False]*v_count
    edges = []
    for i in range(0, v_count):
        edges.append([0]*v_count)
    generate_adj(0, adj, visited, edges, max_w)
    desconected = [i for i in range(0, len(adj)) if len(adj[i]) == 0]
    while(len(desconected) > 0):
        connected = [i for i in range(0, len(adj)) if len(adj[i]) > 0]
        node = rnd.randint(0, len(connected)-1)
        edges[connected[0]][node] = edges[node][connected[0]] = rnd.randint(1, max_w)
        adj[connected[0]].append(node)
        adj[node].append(connected) 
        generate_adj(desconected[0], adj, visited, edges, max_w)
        desconected = [i for i in range(0, len(adj)) if len(adj[i]) == 0]

        
    return adj, edges



def generate_adj(pos: int, adj: list[list[int]], visited: list[bool], edges: list[list[int]], max_w):
    if visited[pos]: return
    count = len(adj[pos])
    if count == 0:
        adj_count = rnd.randint(1, len(adj)-1)  
    else: 
        adj_count = algo = rnd.randint(0, len(adj)- len(adj[pos]) -1)
    for i in range(0, adj_count):
        not_connected = [n for n in range(0, len(edges[pos])) if edges[pos][n] == 0 and n != pos]
        connect = not_connected[rnd.randint(0, len(not_connected) -1)]
        edges[pos][connect] = edges[connect][pos] = rnd.randint(1, max_w)
        adj[pos].append(connect)
        adj[connect].append(pos)
        if not visited[connect]: 
            visited[connect] = True
            generate_adj(connect, adj, visited, edges, max_w)




#print(genrate_conected_graph(10, 10)[1])


def minimun_path(vertex:int, adj: list[list[int]], edges: list[list[int]]):
    result:list[set[tuple[int, int]]] = []*len(adj)
    for _ in adj: result.append(set())
    recursive_min(vertex, adj, edges, [False]*len(adj), result, [0]+[math.inf]*(len(adj)), 0)
    return result


def recursive_min(vertex, adj: list[list[int]], edges: list[list[int]], visited: list[bool], result: list[set[tuple[int,int]]], minim: list[int], distance: int):
    if vertex == 0: visited[vertex] = True
    for adjacent in adj[vertex]:
        if visited[adjacent]: continue
        if minim[adjacent] == (distance+edges[adjacent][vertex]):
            result[adjacent].add((vertex, adjacent))
            result[adjacent].union(result[vertex])
        elif minim[adjacent] > (distance+ distance+edges[adjacent][vertex]):
            tup: tuple = (vertex, adjacent)
            result[adjacent] = set().union(result[vertex])
            result[adjacent].add(tup)
            minim[adjacent] = distance+edges[adjacent][vertex]
        else: continue
        visited[adjacent] = True
        recursive_min(adjacent, adj, edges, visited, result, minim, distance+edges[adjacent][vertex])
    visited[vertex] = False





adjacents = [
    [(1,25), (5, 5)],
    [(0, 25), (8, 5)],
    [(5, 10), (8, 10), (3, 3), (4,30)],
    [(2, 3), (4,27)],
    [(2,30), (3,27)],
    [(0,5),(2, 10),(6, 30)],
    [(5, 30), (7, 1)],
    [(6, 1)],
    [(1, 5), (2, 10)]
    ]




test = []*len(adjacents)
for _ in adjacents: test.append([])

edges_test = []*len(adjacents)
for _ in adjacents: edges_test.append([0]*len(adjacents)) 

for i in range(0, len(adjacents)):
    for ad, dist in adjacents[i]:
        test[i].append(ad)
        edges_test[i][ad] = dist




var = minimun_path(0, test, edges_test)
print(var)