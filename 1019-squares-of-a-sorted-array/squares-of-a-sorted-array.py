class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        square=[0]*len(nums)
        for i, num in enumerate(nums):
            square[i]=num**2
        return sorted(square)
    
    