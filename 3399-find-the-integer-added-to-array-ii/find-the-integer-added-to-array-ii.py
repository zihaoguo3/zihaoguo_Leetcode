class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort()
        nums2.sort()
        xs=[]
        xs.append(nums2[0]-nums1[0])
        xs.append(nums2[0]-nums1[1])
        xs.append(nums2[0]-nums1[2])    
        xs.sort()

        for x in xs:
            i,j=0,0
            while i<len(nums1) and j<len(nums2):
                if nums1[i]+x==nums2[j]:
                    i+=1
                    j+=1
                else:
                    i+=1

            if j==len(nums2):
                return x       