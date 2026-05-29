class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n=len(s)
        i=1
        ans=1

        while i<n:
            if ord(s[i])-1==ord(s[i-1]):
                start=i-1
                while i<n and ord(s[i])-1==ord(s[i-1]):
                    i+=1
                length=i-start
                ans=max(ans,length)
            else:
                i+=1
        return ans

            
