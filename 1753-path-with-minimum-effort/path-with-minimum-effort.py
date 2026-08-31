import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        frontier=[(0,0,0)]
        visited=set()
        row, col= len(heights), len(heights[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        while frontier:
            cost, r, c = heapq.heappop(frontier)

            if (r,c) in visited:
                continue
            
            visited.add((r,c))

            if r==row-1 and c==col-1:
                return cost
            
            for dr, dc in directions:
                nr=r+dr
                nc=c+dc

                if 0<=nr<row and 0<=nc<col:
                    diff=abs(heights[nr][nc]-heights[r][c])
                    curr_effort=max(diff,cost)
                    heapq.heappush(frontier,(curr_effort, nr, nc))
        return 0

                    