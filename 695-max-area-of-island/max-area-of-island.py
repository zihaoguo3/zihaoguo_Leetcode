class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row=len(grid)
        col=len(grid[0])
        max_area=0

        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]==0:
                return 0

            grid[r][c]=0
            area=1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
            return area
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    curr_area=dfs(r,c)
                    max_area=max(max_area,curr_area)
        return max_area

        

        