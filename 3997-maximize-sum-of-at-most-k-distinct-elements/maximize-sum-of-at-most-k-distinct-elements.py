class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_list=list(set(nums))
        nums_list.sort(reverse=True)
        return nums_list[:k]
                
            
            
