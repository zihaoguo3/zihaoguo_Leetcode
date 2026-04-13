class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_left=[0]*len(nums)
        sum_right=[0]*len(nums)

        for i in range(1,len(nums)):
            sum_left[i]+=sum_left[i-1]+nums[i-1]
        
        for j in range(len(nums)-2,-1,-1):
            sum_right[j]+=sum_right[j+1]+nums[j+1]
        
        for i in range(len(nums)):
            if sum_left[i]==sum_right[i]:
                return i
        
        return -1
