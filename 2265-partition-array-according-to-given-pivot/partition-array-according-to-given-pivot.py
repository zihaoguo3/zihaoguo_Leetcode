class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less=[]
        equal=[]
        more=[]

        for num in nums:
            if num>pivot:
                more.append(num)
            elif num<pivot:
                less.append(num)
            else:
                equal.append(num)
        
        less.extend(equal)
        less.extend(more)
        return less
            
        