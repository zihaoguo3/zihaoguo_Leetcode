class Solution(object):
    def hasSpecialSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n=len(s)
        i=0

        while i<n:
            j=i
            while j<n and s[j]==s[i]:
                j+=1
            length=j-i
            if length==k:
                return True
            i=j
        return False
        