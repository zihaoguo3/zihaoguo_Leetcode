class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        start=0
        end=n-1
        area=0

        while start<end:
            tall=min(height[start],height[end])
            width=end-start
            area=max(area,tall*width)
            if height[end]>height[start]:
                start+=1
            else:
                end-=1
        return area

        