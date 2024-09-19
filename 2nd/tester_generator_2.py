import random as rnd


def genrate_conected_graph(max_len, max_w):
    v_count = rnd.randint(0, max_len)
    adj = []
    for i in range(0, v_count):
        adj.append([])
    visited = [False]*v_count
    edges = []
    for i in range(0, v_count):
        edges.append([0]*v_count)
    generate_adj(0, adj, visited, edges, max_w)
    return adj, edges



def generate_adj(pos: int, adj: list[list[int]], visited: list[bool], edges: list[list[int]], max_w):
    adj_count = rnd.randint(1, len(adj)-1) if len(adj[pos]) == 0 else rnd.randint(0, len(adj)- len(adj[pos]) -1)
    for i in range(0, adj_count):
        not_connected = [n for n in range(0, len(edges[pos])) if not edges[pos][n] and n != pos]
        connect = not_connected[rnd.randint(0, len(not_connected) -1)]
        edges[pos][connect] = edges[connect][pos] = rnd.randint(1, max_w)
        adj[pos].append(connect)
        adj[connect].append(pos)
        if not visited[connect]: 
            visited[connect] = True
            generate_adj(connect, adj, visited, edges, max_w)




print(genrate_conected_graph(10, 10)[1])