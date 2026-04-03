class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        ans=[]


        for i in range(n-2):
            x=nums[i]
            start=i+1
            end=n-1
            if i>0 and nums[i-1]==x:
                continue 
            
            while start<end:
                if x+nums[start]+nums[end]<0:
                    start+=1
                elif x+nums[start]+nums[end]>0:
                    end-=1
                else:
                    ans.append([x,nums[start],nums[end]])
                    start+=1
                    while start<end and nums[start]==nums[start-1]:
                        start+=1
                    end-=1
                    while start<end and nums[end]==nums[end+1]:
                        end-=1
        return ans


                
            

