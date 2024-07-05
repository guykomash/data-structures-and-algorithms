import sys
import os

# Adjust the path to the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from datastructures.graphs.directed_graph import DirectedGraph

# def DFSVisit(self, v, visited):
#         visited.add(v)
#         print(v, end=' ')

#         # Recur for all the vertices
#         # adjacent to this vertex
#         for neighbour in self.graph[v]:
#             if neighbour not in visited:
#                 self.DFSVisit(neighbour, visited)

# def DFSRec(self):
#     visited = set()
#     for v in self.graph.keys():
#             if v not in visited:
#                 self.DFSVisit(v, visited)

# def BFS(self):
#     visited = set()
#     for v in self.graph.keys():
#         if v not in visited:
#             visited.add(v)
#             stack = [v]
#             while stack:
#                 u = stack.pop(0)
#                 print(f"{u}, ",end=" ")
#                 for neighbor in self.graph.get(u, []):
#                     if neighbor not in visited:
#                         # visited.add(neighbor)
#                         stack.append(neighbor)

# # Add feature to call "Cycle detected!" when discoverd a back edge.
# def DFS(self):
#     visited = set()
#     for v in self.graph.keys():
#         if v not in visited:
#             pathHistory = set()
#             self.visit(v, visited, pathHistory)
        

# def visit(self, v, visited, pathHistory):
#     print(f"{v}, ",end=" ")
#     visited.add(v)
#     pathHistory.add(v)
#     for neighbor in self.graph.get(v, []):
#         if neighbor not in visited:
#             self.visit(neighbor, visited,pathHistory)
#         # if visited -> check if it is in the pathHistory
#         elif neighbor in pathHistory:
#             print("Found Cycle")





if __name__ == "__main__":
    graph = DirectedGraph()
    print(graph.graph)