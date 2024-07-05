from collections import defaultdict

class DirectedGraph:
    def __init__ (self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        # add edge from u to v
        self.graph[u].append(v)
    
    
if __name__ == "__main__":
    g = DirectedGraph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(5, 0)
    