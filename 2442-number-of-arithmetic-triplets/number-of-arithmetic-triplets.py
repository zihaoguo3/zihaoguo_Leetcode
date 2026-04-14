class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        nums.sort()
        j=1
        k=2
        count=0

        for i in range(len(nums)):
            while j<len(nums) and nums[j]<nums[i]+diff:
                j+=1
            if j<len(nums) and nums[j]-nums[i]==diff:
                while k<len(nums) and nums[k]<nums[j]+diff:
                    k+=1
                if k<len(nums) and nums[k]-nums[j]==diff:
                    count+=1
        return count            
            

        