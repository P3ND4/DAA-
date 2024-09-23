from collections import defaultdict 

class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = defaultdict(list) 

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def PPROX_VERTEX_COVER(self):
        visited = [False] * self.V
        
        for u in range(self.V):
            if not visited[u]:
                for v in self.graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        visited[u] = True
                        break

        # Return the vertex cover instead of printing it
        return [j for j in range(self.V) if visited[j]]

def createGraph(colors, manufacturers):
    color_to_vertices = defaultdict(list)
    
    # Map each color to its corresponding vertices
    for idx, (color, manufacturer_list) in enumerate(zip(colors, manufacturers)):
        color_to_vertices[color].append(idx)
    
    # Number of vertices
    num_vertices = len(colors)
    g = Graph(num_vertices)
    
    # Add edges based on the conditions
    for color, vertices in color_to_vertices.items():
        # Connect vertices of the same color
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                g.addEdge(vertices[i], vertices[j])
    
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            # Connect if they do not share any manufacturers
            if not set(manufacturers[i]) & set(manufacturers[j]):
                g.addEdge(i, j)
    
    return g

def findLargestIndependentSet(g):
    vertex_cover = g.PPROX_VERTEX_COVER()
    # The independent set is the complement of the vertex cover
    return [v for v in range(g.V) if v not in vertex_cover]

# Example usage
colors = ['red', 'blue', 'red', 'green', 'blue', 'green']
manufacturers = [['A'], ['B'], ['A'], ['C'], ['B'], ['D']]
k = 3

g = createGraph(colors, manufacturers)

independent_set = findLargestIndependentSet(g)

if len(independent_set) >= k:
    print("Existe una alianza multicolor.")
else:
    print("No existe una alianza multicolor.")

