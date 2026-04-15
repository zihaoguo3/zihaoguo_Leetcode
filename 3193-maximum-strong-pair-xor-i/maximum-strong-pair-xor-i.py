class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor=0
        n=len(nums)

        for i in range(n):
            for j in range(n):
                if abs(nums[j]-nums[i])<=min(nums[j],nums[i]):
                    max_xor=max(max_xor,nums[j]^nums[i])
                    
        return max_xor