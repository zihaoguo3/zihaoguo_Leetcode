class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        left=0
        right=n-1
        ans=0
        mod=10**9+7
        while left<=right:
            if nums[left]+nums[right]<=target:
                ans=(ans + pow(2, right - left, mod)) % mod
                left+=1
            else:
                right-=1
        return ans
