class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0

        for i in range(len(nums)):
            if nums[i]!=2:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1


        j=0
        for i in range(l):
            if nums[i]==0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums
        