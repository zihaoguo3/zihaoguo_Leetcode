class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=-1
        left, right = 0, len(nums)-1
        nums.sort()
        while left<right:
            ans=max(ans,nums[left]+nums[right])
            left+=1
            right-=1
        return ans 

        