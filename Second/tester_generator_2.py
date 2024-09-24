import random as rnd
import math
import json
from tester import deserialize

def tester_generator(n=100, max_len=30, max_w = 100):
    test_cases = []
    first = n

    while(n):
        adj, edges = genrate_conected_graph(max_len, max_w)
        result: list[list] = []
        for _ in adj: result.append([])
        for i in range(0, len(adj)):
            path = minimun_path(i, adj, edges)
            for j in range(0, len(adj)):
                if i == j:
                    result[i].append(0)
                    continue
                result[i].append(len(path[j])) 
        
        test_case = {
            "test_case": f'{first-n+1}',
            "adj": [[str(x) for x in y] for y in adj],
            "edges": [[str(x) for x in y] for y in edges],
            "result": [[str(x) for x in y] for y in result]
        }
        test_cases.append(test_case)   
        n -= 1           
    with open('Second/test_cases_2.json', 'w') as f:
        json.dump(test_cases, f, indent=2)



def adj_list_build(edges: list[list[int]]):
    new_adj_list = []
    for _ in edges: new_adj_list.append([])

    for i in range(0, len(edges)):
        for j in range(0, len(edges)):
            if edges[i][j]:
                new_adj_list[i].append(j)
    return new_adj_list

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
        for i in range(0, len(adj)):
            del edges[i][desconected[0]]
        del edges[desconected[0]]
        del adj[desconected[0]]
        desconected = [i for i in range(0, len(adj)) if len(adj[i]) == 0]
    adj = adj_list_build(edges)
        
    return adj, edges



def generate_adj(pos: int, adj: list[list[int]], visited: list[bool], edges: list[list[int]], max_w):
    if pos == 0: visited[pos] = True
    count = len(adj[pos])
    if count == 0:
        adj_count = rnd.randint(1, len(adj)-1)  
    else: 
        adj_count = algo = rnd.randint(0, len(adj)- len(adj[pos]) -1)
    for i in range(0, adj_count):
        not_connected = [n for n in range(0, len(adj)) if not n in adj[pos] and n != pos]
        if len(not_connected) == 0: continue
        rand = rnd.randint(0, len(not_connected) -1)
        connect = not_connected[rand]  
        
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
    distance = [math.inf]*len(adj)
    distance[vertex] = 0
    recursive_min(vertex, vertex, adj, edges, [False]*len(adj), result,distance, 0)
    return result


def recursive_min(initial_ver, vertex, adj: list[list[int]], edges: list[list[int]], visited: list[bool], result: list[set[tuple[int,int]]], minim: list[int], distance: int):
    if vertex == initial_ver: visited[vertex] = True
    for adjacent in adj[vertex]:
        if visited[adjacent]: continue
        if minim[adjacent] == (distance+edges[adjacent][vertex]):
            temp = set()
            temp.add((max(vertex, adjacent), min(vertex, adjacent)))
            result[adjacent] = result[adjacent].union(temp)
            result[adjacent] = result[adjacent].union(result[vertex])
        elif minim[adjacent] > (distance+ edges[adjacent][vertex]):
            tup: tuple = ((max(vertex, adjacent), min(vertex, adjacent)))
            result[adjacent] = set().union(result[vertex])
            result[adjacent].add(tup)
            minim[adjacent] = distance+edges[adjacent][vertex]
        else: continue
        visited[adjacent] = True
        recursive_min(initial_ver, adjacent, adj, edges, visited, result, minim, distance+edges[adjacent][vertex])
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




adj_2 = [
      [
        "4",
        "5",
        "7"
      ],
      [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "9"
      ],
      [
        "1",
        "4",
        "5",
        "6",
        "7",
        "9"
      ],
      [
        "1",
        "4",
        "5",
        "6",
        "7"
      ],
      [
        "0",
        "1",
        "2",
        "3",
        "5",
        "7",
        "8",
        "9"
      ],
      [
        "0",
        "1",
        "2",
        "3",
        "4",
        "6",
        "7",
        "8",
        "9"
      ],
      [
        "1",
        "2",
        "3",
        "5",
        "7",
        "9"
      ],
      [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "8",
        "9"
      ],
      [
        "4",
        "5",
        "7"
      ],
      [
        "1",
        "2",
        "4",
        "5",
        "6",
        "7"
      ]
    ]








edges_2 =  [
      [
        "0",
        "0",
        "0",
        "0",
        "1",
        "6",
        "0",
        "5",
        "0",
        "0"
      ],
      [
        "0",
        "0",
        "4",
        "9",
        "3",
        "10",
        "9",
        "8",
        "0",
        "9"
      ],
      [
        "0",
        "4",
        "0",
        "0",
        "8",
        "4",
        "6",
        "3",
        "0",
        "6"
      ],
      [
        "0",
        "9",
        "0",
        "0",
        "6",
        "1",
        "8",
        "9",
        "0",
        "0"
      ],
      [
        "1",
        "3",
        "8",
        "6",
        "0",
        "9",
        "0",
        "7",
        "5",
        "1"
      ],
      [
        "6",
        "10",
        "4",
        "1",
        "9",
        "0",
        "4",
        "9",
        "1",
        "1"
      ],
      [
        "0",
        "9",
        "6",
        "8",
        "0",
        "4",
        "0",
        "1",
        "0",
        "4"
      ],
      [
        "5",
        "8",
        "3",
        "9",
        "7",
        "9",
        "1",
        "0",
        "1",
        "4"
      ],
      [
        "0",
        "0",
        "0",
        "0",
        "5",
        "1",
        "0",
        "1",
        "0",
        "0"
      ],
      [
        "0",
        "9",
        "6",
        "0",
        "1",
        "1",
        "4",
        "4",
        "0",
        "0"
      ]
    ]
    





var = minimun_path(1, deserialize(adj_2), deserialize(edges_2))
print(var)
#tester_generator(n= 1000, max_len=10, max_w=10)
#res, _ = genrate_conected_graph(10, 10)
#print(var)