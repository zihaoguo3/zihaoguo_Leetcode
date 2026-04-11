class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        MOD = 10**9 + 7
        arr=[]
        for i in range(n):
            curr_sum=0
            for j in range(i,n):
                curr_sum+=nums[j]
                arr.append(curr_sum)
        
        arr.sort()
        result=sum(arr[left-1:right])%MOD
        return result