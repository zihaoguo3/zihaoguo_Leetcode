class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        ans=[]
        ans.append(s[:spaces[0]])
        
        for i in range(1,len(spaces)):
            ans.append(s[spaces[i-1]:spaces[i]])
        
        ans.append(s[spaces[-1]:])
        
        return ' '.join(ans)

        