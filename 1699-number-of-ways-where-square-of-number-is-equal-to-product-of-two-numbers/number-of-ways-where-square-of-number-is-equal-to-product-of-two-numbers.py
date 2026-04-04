class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n1=len(nums1)
        n2=len(nums2)
        ans=0
        dict1=defaultdict(int)
        dict2=defaultdict(int)

        for i in range(n1-1):
            for j in range(i+1,n1):
                dict1[nums1[i]*nums1[j]]+=1

        for i in range(n2-1):
            for j in range(i+1,n2):
                dict2[nums2[i]*nums2[j]]+=1
        
        for num1 in nums1:
            target=num1**2
            ans+=dict2[target]
        for num2 in nums2:
            target=num2**2
            ans+=dict1[target]
        return ans
        