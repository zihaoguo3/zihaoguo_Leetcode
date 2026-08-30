from collections import deque
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        queue=deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    queue.append((i,j,0))
        
        if len(queue)==0 or len(queue)==n*n:
            return -1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        max_dist=-1

        while queue:
            r,c, dist=queue.popleft()
            max_dist=max(dist,max_dist)
            for dr, dc in directions:
                nr, nc= r+dr, c+dc
                if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0:
                    grid[nr][nc]=1
                    queue.append((nr,nc,dist+1))
        return max_dist



        