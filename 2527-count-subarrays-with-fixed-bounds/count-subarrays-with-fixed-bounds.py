class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        ans=0

        min_index=-1
        max_index=-1
        wall=-1

        for i, num in enumerate(nums):
            if not minK<=num<=maxK:
                wall=i
            if num==minK:
                min_index=i
            if num==maxK:
                max_index=i
            
            count=min(min_index,max_index)-wall
            ans+=max(count,0)
        return ans
        