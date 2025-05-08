class Solution:
    # def isReachable(adj, src, dest, n):
      
    def validPath(self, n: int, edges: List[List[int]], src: int, dest: int) -> bool:
        if n <=0 :
            return False
        if src == dest:
            return True
        visited = [False] * n
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        queue = deque()
        visited[src] = True
        queue.append(src)

        while queue:
            src = queue.popleft()
            for i in adj[src]:
                print(i)
                if i == dest:
                    return True
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    
        return False

