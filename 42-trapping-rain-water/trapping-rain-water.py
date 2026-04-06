class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left=0
        right=n-1
        ans=0
        left_max=height[left]
        right_max=height[right]

        while left<right:
            if left_max<right_max:
                left+=1
                left_max=max(left_max,height[left])
                ans+=left_max-height[left]

            else:
                right-=1
                right_max=max(right_max,height[right])
                ans+=right_max-height[right]
        return ans




        