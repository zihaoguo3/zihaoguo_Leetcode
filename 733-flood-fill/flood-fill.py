class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        row=len(image)
        col=len(image[0])
        s=image[sr][sc]
        visited=set()

        def dfs(r,c):
            if (r,c) in visited or r<0 or r>=row or c<0 or c>=col or image[r][c]!=s:
                return 
            image[r][c]=color
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        dfs(sr,sc)
        return image
        