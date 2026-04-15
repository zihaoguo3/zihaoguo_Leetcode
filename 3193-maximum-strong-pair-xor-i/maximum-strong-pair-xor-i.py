class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_xor=0

        l=0

        n=len(nums)

        for r, x in enumerate(nums):
            while abs(nums[l]-nums[r])>min(nums[l],nums[r]):
                l+=1
            
            for i in range(l,r+1):
                max_xor=max(max_xor,nums[i]^x)
        return max_xor