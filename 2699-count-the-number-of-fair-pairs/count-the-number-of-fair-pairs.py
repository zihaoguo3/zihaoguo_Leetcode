class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        
        def solve(target):
            start=0
            end=len(nums)-1

            count=0

            while start<end:
                s=nums[start]+nums[end]
                if s<=target:
                    count+=(end-start)
                    start+=1
                else:
                    end-=1
            return count
        return solve(upper)-solve(lower-1)

        