class Solution(object):
    def perfectPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            nums[i]=abs(nums[i])
    
            
        nums.sort()
        i=0
        j=i+1
        count=0

        for i in range(n):
            if j<=i:
                j=i+1
            
            while j<n and nums[j]<=2*nums[i]:
                j+=1
            count+=(j-i-1)
        return count