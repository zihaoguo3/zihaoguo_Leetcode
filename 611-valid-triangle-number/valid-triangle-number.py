class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        count=0

        for i in range(n-1,1,-1):
            start=0
            end=i-1
            while start<end:
                if nums[start]+nums[end]>nums[i]:
                    count+=(end-start)
                    end-=1
                else:
                    start+=1
        return count
                



        