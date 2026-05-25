class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def isSubsequence(s1, s2):
            i,j=0,0

            while i<len(s1) and j<len(s2):
                if s1[i]==s2[j]:
                    i+=1
                j+=1
            return i==len(s1)
        strs.sort(key=len, reverse=True)

        
        for i, s1 in enumerate(strs):
            is_uncommon = True
            for j, s2 in enumerate(strs):
                if i==j:
                    continue
                if isSubsequence(s1,s2):
                    is_uncommon = False
                    break 
            if is_uncommon:
                return len(s1)
        return -1
        