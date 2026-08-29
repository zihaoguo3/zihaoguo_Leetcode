from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row, col= len(mat), len(mat[0])
        queue=deque()

        for r in range(row):
            for c in range(col):
                if mat[r][c]==0:
                    queue.append((r,c))
                else:
                    mat[r][c]=-1
        
        while queue:
            r,c=queue.popleft()
            for dr, dc in directions:
                nr, nc=r+dr, c+dc
                if 0<=nr<row and 0<=nc<col and mat[nr][nc]==-1:
                    mat[nr][nc]=mat[r][c]+1
                    queue.append((nr,nc))
        return mat
        