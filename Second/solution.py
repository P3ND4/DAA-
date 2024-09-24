import math

def min_path(adj: list[list[tuple[int, int]]]) -> list[list[int]]:
  matrix = build_matrix(len(adj))
  visited = [False]*len(adj)
  visited[0] = True
  min_path_rec(adj, matrix, [0], visited, 0)  
  
  for i in range(len(matrix)):
    matrix[i] = list(map(lambda x: x[0], matrix[i]))
  
  return matrix
    
def build_matrix(size: int) -> list[list[tuple]]:
  temp = []
  
  for i in range(size):
    temp.append([math.inf] * size)
    
    for j in range(size):
      temp[i][j] = (math.inf, set()) if i != j else (0, set())
      
  return temp

def min_path_rec(adj: list[list[tuple[int, int]]], matrix: list[list[tuple]], nodes_adds: list, visited: list[bool], head: int): 
  for element in adj[head]:  
    node = element[0]
    e = element[1]
    
    if not visited[node]:
      nodes_adds.append(node)
      visited[node] = True
      fix_adj(head, adj[node])
    
      for x in nodes_adds[:-1]:
        aux = set(matrix[x][head][1])
        aux.add((min(head, node), max(head, node)))
        matrix[x][node] = (matrix[x][head][0] + e, aux) 
      
      for x in nodes_adds[:-1]:
        matrix[node][x] = (matrix[x][node][0], matrix[x][node][1])
        
      min_path_rec(adj, matrix, nodes_adds, visited, node)
    
    else:
      for x in nodes_adds:
        if x != head:
          if matrix[x][head][0] >= matrix[x][node][0] + e:
            aux = set(matrix[x][node][1])
            aux.add((min(head, node), max(head, node)))
            
            if matrix[x][head][0] == matrix[x][node][0] + e:
              matrix[x][head] = (matrix[x][node][0] + e, matrix[x][head][1].union(aux))
              matrix[head][x] = (matrix[x][node][0] + e, matrix[head][x][1].union(aux))
            
            else:
              matrix[x][head] = (matrix[x][node][0] + e, aux)
              matrix[head][x] = (matrix[x][node][0] + e, aux)

          elif matrix[x][node][0] >= matrix[x][head][0] + e:
            aux = set(matrix[x][head][1])
            aux.add((min(head, node), max(node, head)))
            
            if matrix[x][node][0] == matrix[x][head][0] + e:
              matrix[x][node] = (matrix[x][head][0] + e, matrix[x][node][1].union(aux))
              matrix[node][x] = (matrix[x][head][0] + e, matrix[node][x][1].union(aux))
              
            else:
              matrix[x][node] = (matrix[x][head][0] + e, aux)
              matrix[node][x] = (matrix[x][head][0] + e, aux)

def fix_adj(head: int, l: list[tuple]):
  for i in range(len(l)):
    if l[i][0] == head:
      aux = l[i]
      del l[i]
      l.append(aux)
      return
