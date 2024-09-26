import math

def floyd_warshall(adj: list[list[tuple[int, int]]]) -> list[list[int]]:
  matrix = build_matrix(adj)
  
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      if j != i and matrix[i][j][0] < math.inf:
        for k in range(len(matrix)):
          if (k != j) and (k != i) and (matrix[j][k][0] >= matrix[i][j][0] + matrix[i][k][0]) and (matrix[i][j][0] + matrix[i][k][0] < math.inf):
            aux = set(matrix[i][j][1])
            aux = aux.union(matrix[i][k][1])
            
            if matrix[j][k][0] == matrix[i][j][0] + matrix[i][k][0]:
              matrix[j][k] = (matrix[j][k][0], matrix[j][k][1].union(aux))
            
            else:
              matrix[j][k] = (matrix[i][j][0] + matrix[i][k][0], aux)
  
  for i in range(len(matrix)):
    matrix[i] = list(map(lambda x: len(x[1]), matrix[i]))
              
  return matrix
                 
def build_matrix(adj: list[list[tuple[int, int]]]) -> list[list[tuple]]:
  temp = []
  
  for i in range(len(adj)):
    temp.append([math.inf] * len(adj))
    
    for j in range(len(adj)):
      temp[i][j] = (math.inf, set()) if i != j else (0, set())
      
  for i in range(len(adj)):
    for e in adj[i]:
      temp[i][e[0]] = (e[1], set(((min(e[0], i), max(e[0], i)),)))
      
  return temp
  