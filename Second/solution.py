import math

def min_path(adj: list[list[tuple[int, int]]]) -> list[list[int]]:
  matrix = build_matrix(len(adj))
  visited = [False]*len(adj)
  visited[0] = True
  min_path_rec(adj, matrix, [0], visited, 0)  
  
  for i in range(len(matrix)):
    matrix[i] = list(map(lambda x: len(x[1]), matrix[i]))
  
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
              fix_path(matrix, nodes_adds, x, node)
            
            else:
              matrix[x][head] = (matrix[x][node][0] + e, aux)
              matrix[head][x] = (matrix[x][node][0] + e, aux)
              fix_path(matrix, nodes_adds, x, node)

          elif matrix[x][node][0] >= matrix[x][head][0] + e:
            aux = set(matrix[x][head][1])
            aux.add((min(head, node), max(node, head)))
            
            if matrix[x][node][0] == matrix[x][head][0] + e:
              matrix[x][node] = (matrix[x][head][0] + e, matrix[x][node][1].union(aux))
              matrix[node][x] = (matrix[x][head][0] + e, matrix[node][x][1].union(aux))
              fix_path(matrix, nodes_adds, x, head)
              
            else:
              matrix[x][node] = (matrix[x][head][0] + e, aux)
              matrix[node][x] = (matrix[x][head][0] + e, aux)
              fix_path(matrix, nodes_adds, x, head)

def fix_path(matrix: list[list[tuple]], nodes: list, start: int, inter: list):
  for node in nodes:
    if node != start:
      if matrix[start][node][0] >= matrix[start][inter][0] + matrix[inter][node][0]:
        aux = set(matrix[start][inter][1])
        aux = aux.union(matrix[inter][node][1])

        if matrix[start][node][0] == matrix[start][inter][0] + matrix[inter][node][0]:
          matrix[start][node] = (matrix[start][node][0], matrix[start][node][1].union(aux))
          matrix[node][start] = (matrix[start][node][0], matrix[start][node][1].union(aux))

        else:
          matrix[start][node] = (matrix[start][inter][0] + matrix[inter][node][0], aux)
          matrix[node][start] = (matrix[start][inter][0] + matrix[inter][node][0], aux)
      