class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        ans=float('inf')

        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            start=i+1
            end=n-1
            while start<end:
                s=nums[i]+nums[start]+nums[end]
                if s==target:
                    return target
                if abs(ans-target)>abs(s-target):
                    ans=s
                if s>target:
                    end-=1
                elif s<target:
                    start+=1
    
        return ans
                