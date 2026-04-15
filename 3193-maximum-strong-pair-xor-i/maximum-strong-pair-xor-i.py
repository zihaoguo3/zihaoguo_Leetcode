class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_xor=0
        n=len(nums)
        l=0

        for r in range(n):
            while abs(nums[r]-nums[l])>min(nums[l],nums[r]):
                l+=1
            for i in range(l,r+1):
                max_xor=max(max_xor,nums[i]^nums[r])

                    
        return max_xor