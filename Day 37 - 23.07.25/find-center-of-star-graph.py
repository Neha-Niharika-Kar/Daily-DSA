# GRAPHS - Easy

# There is an undirected star graph consisting of n nodes labeled from 1 to n. 
# A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. 
# Return the center of the given star graph.

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        nodes = [0] * (n+1)
        
        for i,j in edges:
            nodes[i] += 1
            nodes[j] += 1
        
        for i in range(1, n+1):
            if nodes[i] == n-1:
                return i

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0]
        c, d = edges[1]

        if a == c or a == d:
            return a
        return b
