class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        l=0
        count=0

        for r in range(len(nums)):
            while nums[r]-nums[l]>1:
                l+=1
            if nums[r]-nums[l]==1:
                count=max(count,r-l+1)
        return count
            



        