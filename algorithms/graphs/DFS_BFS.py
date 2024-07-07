import sys
import os

# Adjust the path to the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from datastructures.graphs import DirectedGraph


# Add feature to call "Cycle detected!" when discoverd a back edge.
def DFS(graph):
    visited = set()
    for v in graph.keys():
        if v not in visited:
            pathHistory = set()
            print("start",end="")
            visit(v, visited, pathHistory, graph)
            print("\n")

def visit(v, visited, pathHistory,graph):
    print(f" -> {v}, ",end=" ")
    visited.add(v)
    pathHistory.add(v)
    for neighbor in graph.get(v, []):
        if neighbor not in visited:
            visit(neighbor, visited, pathHistory, graph)
        # if visited -> check if it is in the pathHistory
        elif neighbor in pathHistory:
            print("Found Cycle")

    # finished with v and all his neighbors. discard form the current opened path
    pathHistory.discard(v)

def BFS(graph):
    visited = set()
    for v in graph.keys():
        if v not in visited:
            q = [v]
            visited.add(v)
            while q:
                u = q.pop(0)
                print(f" => {u}", end="")
                negihbors = graph.get(u, [])
                for neighbor in negihbors:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)

if __name__ == "__main__":
    g = DirectedGraph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(5, 6)
    g.addEdge(6, 7)
    g.addEdge(8, 7)
    g.addEdge(8, 9)
    BFS(g.graph)