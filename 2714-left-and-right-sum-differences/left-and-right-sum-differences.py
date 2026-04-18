class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        left_sum=[0]*n
        right_sum=[0]*n
        final=[0]*n

        for i in range(1,n):
            left_sum[i]=nums[i-1]+left_sum[i-1]
        for i in range(n-2,-1,-1):
            right_sum[i]=nums[i+1]+right_sum[i+1]
        
        for i in range(n):
            final[i]=abs(left_sum[i]-right_sum[i])
        return final
            
        
        
