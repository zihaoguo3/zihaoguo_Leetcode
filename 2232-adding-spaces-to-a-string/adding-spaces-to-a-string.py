class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """

        ans=[]

        ans.append(s[:spaces[0]])
        prev=0
        for i in range(1,len(spaces)):
            ans.append(s[spaces[prev]:spaces[i]])
            prev+=1
        ans.append(s[spaces[prev]:])
        return (" ".join(ans))
            


        