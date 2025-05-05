class Solution:
    # def createAdj(self, graph, V):
    #     adjList = [[] for _ in range(V)]
    #     for edge in graph:
    #         print(edge)
    #         u, v = edge
    #         adjList[u].append(v)
    #         adjList[v].append(u)
    #     return adjList

    def dfs(self, u, color, colors, adj):
        from collections import deque

        colors[u] = color
        for v in adj[u]:
            if colors[v] == -1:
                if not self.dfs(v, 1 - color, colors, adj):
                    return False
            elif colors[v] == color:
                return False
        return True


    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        colors = [-1] * V
        # adj_list = self.createAdj(graph, V)
        for i in range(V):
            if colors[i] == -1:
                if not self.dfs(i, 0, colors, graph):
                    return False
        
        return True


        
