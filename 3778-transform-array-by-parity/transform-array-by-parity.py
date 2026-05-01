class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i,num in enumerate(nums):
            if num%2==0:
                nums[i]=0
            else:
                nums[i]=1
        return sorted(nums)

        