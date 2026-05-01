class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        
        j=0

        for i, num in enumerate(nums):
            if num!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums
        