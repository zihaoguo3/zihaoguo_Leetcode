class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        count={}

        for nums in nums1:
            count[nums[0]]=nums[1]
        
        for nums in nums2:
            count[nums[0]]=count.get(nums[0],0)+nums[1]
        
        merge=[]

        for key, value in sorted(count.items()):
            merge.append([key,value])
        
        return merge
        