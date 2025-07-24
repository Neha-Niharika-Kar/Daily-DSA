# GRAPHS - Easy

# Given a connected undirected graph containing V vertices, represented by a 2-d adjacency list adj[][], 
# where each adj[i] represents the list of vertices connected to vertex i. 
# Perform a Breadth First Search (BFS) traversal starting from vertex 0, visiting vertices from left to right according to the given adjacency list, 
# and return a list containing the BFS traversal of the graph.
# Do traverse in the same order as they are in the given adjacency list.

from collections import deque
class Solution:
    def bfs(self, adj):
        visited = set()
        queue = deque([0])
        bfs = []
        
        while queue:
            node = queue.popleft()
            
            if node not in visited:
                bfs.append(node)
                visited.add(node)
                
                for i in adj[node]:
                    if i not in visited:  
                        queue.append(i)
            
        return bfs
