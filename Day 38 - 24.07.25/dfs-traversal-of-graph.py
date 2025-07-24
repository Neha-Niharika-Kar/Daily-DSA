# GRAPHS - Easy

# Given a connected undirected graph containing V vertices represented by a 2-d adjacency list adj[][], 
# where each adj[i] represents the list of vertices connected to vertex i. 
# Perform a Depth First Search (DFS) traversal starting from vertex 0, visiting vertices from left to right as per the given adjacency list, 
# and return a list containing the DFS traversal of the graph.
# Do traverse in the same order as they are in the given adjacency list.

class Solution:
    def dfs(self, adj):
        visited = set()
        dfs = []
        
        def dfs_g(node):
            if node not in visited:
                dfs.append(node)
                visited.add(node)
                
                for i in adj[node]:
                    if i not in visited:
                        dfs_g(i)
        
        dfs_g(0)
        return dfs
