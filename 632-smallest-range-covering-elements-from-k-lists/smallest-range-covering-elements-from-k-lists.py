class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        min_heap=[]
        curr_max=float('-inf')

        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0],i,0))
            curr_max=max(curr_max,nums[i][0])
        
        ans=[float('-inf'),float('inf')]

        while min_heap:
            number, array, index=heapq.heappop(min_heap)
            curr_min=number
            if curr_max-curr_min<ans[1]-ans[0]:
                ans=[curr_min,curr_max]
            
            if index==len(nums[array])-1:
                return ans
            
            heapq.heappush(min_heap,(nums[array][index+1],array, index+1))
            curr_max=max(curr_max,nums[array][index+1])
