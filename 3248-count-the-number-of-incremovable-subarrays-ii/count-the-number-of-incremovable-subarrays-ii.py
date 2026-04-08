class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        left=0
        while left<n-1 and nums[left+1]>nums[left]:
            left+=1
        
        if left==n-1:
            return n*(n+1)//2

        right=n-1
        while right>0 and nums[right]>nums[right-1]:
            right-=1
        
        ans=n-right+1
        q=right
        for p in range(left+1):

            while q<n and nums[q]<=nums[p]:
                q+=1
            
            ans+= n-q+1
        return ans

        