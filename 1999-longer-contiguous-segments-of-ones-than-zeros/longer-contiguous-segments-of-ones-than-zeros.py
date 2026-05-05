class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        max_1=0
        max_0=0
        curr_1=0
        curr_0=0

        for num in s:
            if num=="1":
                curr_1+=1
                curr_0=0
            elif num=="0":
                curr_0+=1
                curr_1=0
            max_1=max(max_1,curr_1)
            max_0=max(max_0,curr_0)
        return max_1>max_0