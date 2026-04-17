class Solution:
    def maxArea(self, heights):
        n=len(heights)
        left=0
        right=n-1
        max_amount=0

        while left<right:
            s=min(heights[left],heights[right])*(right-left)
            max_amount=max(max_amount,s)                
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_amount
            

        