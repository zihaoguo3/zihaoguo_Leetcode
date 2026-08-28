from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        len_r, len_c=len(maze), len(maze[0])
        
        directions = [(-1, 0),(1, 0), (0, -1),(0, 1)]

        queue=deque([(entrance[0],entrance[1],0)])

        maze[entrance[0]][entrance[1]]='+'

        while queue:
            r, c, length=queue.popleft()

            for dr, dc in directions:
                nr, nc= dr+r, dc+c

                if 0<=nr<len_r and 0<=nc<len_c and maze[nr][nc]=='.':
                    if nr==0 or nr==len_r-1 or nc==0 or nc==len_c-1:
                        return length+1
                    maze[nr][nc]='+'
                    queue.append((nr,nc,length+1))
        return -1
                    
            