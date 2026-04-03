class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()

        n=len(nums)
        ans=[]

        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue

            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                start=j+1
                end=n-1

                while start<end:
                    s=nums[i]+nums[j]+nums[start]+nums[end]
                    if s<target:
                        start+=1
                    elif s>target:
                        end-=1
                    else:
                        ans.append([nums[i],nums[j],nums[start],nums[end]])
                        start+=1
                        end-=1
                        while start<end and nums[start]==nums[start-1]:
                            start+=1
                        while start<end and nums[end]==nums[end+1]:
                            end-=1
        return ans