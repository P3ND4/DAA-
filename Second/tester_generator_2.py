import random as rnd
import math
import json


#########----------Generador de casos de prueba------------------###############################

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


#####################################################################################################


def adj_list_build(edges: list[list[int]]):
    new_adj_list = []
    for _ in edges: new_adj_list.append([])

    for i in range(0, len(edges)):
        for j in range(0, len(edges)):
            if edges[i][j]:
                new_adj_list[i].append(j)
    return new_adj_list


#################---------------Generador de grafos conexos----------------#########################

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

#############################################################################################



###############---------Fuerza Bruta-----------------#####################################

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

#####################################################################################################################







#tester_generator(n= 1000, max_len=10, max_w=10)
