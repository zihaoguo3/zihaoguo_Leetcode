class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        square=[0]*len(nums)
        l=0
        r=len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[l])>abs(nums[r]):
                square[i]=nums[l]**2
                l+=1
            else:
                square[i]=nums[r]**2
                r-=1
        return square

        
    
    