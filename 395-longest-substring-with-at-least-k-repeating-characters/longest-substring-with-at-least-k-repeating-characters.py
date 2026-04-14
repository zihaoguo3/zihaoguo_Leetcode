class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count={}
        if not s or len(s) < k:
            return 0
        for num in s:
            count[num]=count.get(num,0)+1
        
        for char in count:
            if count[char]<k:
                return max(self.longestSubstring(sub,k) for sub in s.split(char))
        return len(s)
        

