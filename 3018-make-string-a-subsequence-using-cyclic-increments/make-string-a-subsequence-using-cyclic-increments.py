class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        i,j=0,0

        while i<len(str1) and j<len(str2):
            c1=str1[i]
            c2=str2[j]
            if c1==c2 or (c1 == 'z' and c2 == 'a') or (chr(ord(c1) + 1) == c2):
                j+=1
            i+=1
        return j==len(str2)