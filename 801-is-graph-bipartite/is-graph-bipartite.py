class Solution:
    # def createAdj(self, graph, V):
    #     adjList = [[] for _ in range(V)]
    #     for edge in graph:
    #         print(edge)
    #         u, v = edge
    #         adjList[u].append(v)
    #         adjList[v].append(u)
    #     return adjList

    # def dfs(self, u, color, colors, adj):
    #     from collections import deque

    #     colors[u] = color
    #     for v in adj[u]:
    #         if colors[v] == -1:
    #             if not self.dfs(v, 1 - color, colors, adj):
    #                 return False
    #         elif colors[v] == color:
    #             return False
    #     return True


    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        colors = [-1] * V
        # # adj_list = self.createAdj(graph, V)
        # for i in range(V):
        #     if colors[i] == -1:
        #         if not self.dfs(i, 0, colors, graph):
        #             return False
        
        for i in range(V):
            if colors[i] == -1:
                colors[i] = 0
                queue = deque([i]) 
                
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    elif colors[u] == colors[v]:
                        return False
        
        return True


        
