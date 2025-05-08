class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        moves = [(0,1),(1,0),(-1,0),(0,-1)]
        distance = [[math.inf] * m for _ in range(n)]
        # distance, i, j
    
        heap = [(0,0,0)]
        while heap:
            time, x, y = heapq.heappop(heap)
            if x == n-1 and y == m-1:
                return time
            for mr, mc in moves:
                nr, nc = x + mr, y + mc
                # next_time = moveTime[nr][nc]
                if 0 <= nr < n and 0 <= nc < m:
                    # cost = (x + y ) % 2 + 1
                    wait = max(time, moveTime[nr][nc]) + ((x + y) % 2 + 1)
                    
                    if wait < distance[nr][nc]:
                        distance[nr][nc] = wait
                        heapq.heappush(heap, (wait, nr, nc))

        return -1