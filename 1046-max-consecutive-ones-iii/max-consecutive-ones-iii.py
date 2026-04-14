class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count={}
        max_count=0
        num_k=0
        l=0
        for r, x in enumerate(nums):
            count[x]=count.get(x,0)+1
            while count.get(0,0)>k:
                count[nums[l]]-=1
                l+=1
            max_count=max(max_count,r-l+1)
        return max_count
            


