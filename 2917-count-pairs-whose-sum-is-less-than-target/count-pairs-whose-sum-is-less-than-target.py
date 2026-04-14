class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        left=0
        right=n-1
        count=0

        while left<right:
            s=nums[left]+nums[right]
            if s<target:
                count+=(right-left)
                left+=1
            else:
                right-=1
        return count


