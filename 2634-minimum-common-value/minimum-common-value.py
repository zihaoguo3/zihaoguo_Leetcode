class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        left, right=0,0

        while left<len(nums1) and right<len(nums2):
            if nums1[left]<nums2[right]:
                left+=1
            elif nums1[left]>nums2[right]:
                right+=1
            else:
                return nums2[right]
        return -1
            
        