import heapq
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        start_r, start_c=0,0
        total_keys=0


        for r in range(row):
            for c in range(col):
                if grid[r][c]=='@':
                    start_r, start_c=r,c
                elif 'a' <= grid[r][c] <= 'f':
                    total_keys+=1
        pq=[(0,start_r, start_c, "")]
        visited=set()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        while pq:
            cost, r, c, keys=heapq.heappop(pq)
            if len(keys)==total_keys:
                return cost
            
            state=(r,c,keys)
            if state in visited:
                continue
            visited.add(state)

            for dr, dc in directions:
                nr, nc= r+dr, c+dc
                if not (0<=nr<row and 0<=nc<col):
                    continue
                cell=grid[nr][nc]
                if cell=="#":
                    continue
                next_keys=keys
                if 'A'<=cell<='F':
                    if cell.lower() not in keys:
                        continue
                elif 'a'<=cell<='f':
                    if cell not in keys:
                        next_keys= "".join(sorted(keys + cell))
                pq.append((cost+1, nr, nc, next_keys))
        return -1


                

            