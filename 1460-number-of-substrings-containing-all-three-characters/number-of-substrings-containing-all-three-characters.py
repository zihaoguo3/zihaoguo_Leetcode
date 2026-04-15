class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        count=Counter()

        l=0

        ans=0

        for r, num in enumerate(s):
            count[num]+=1
            while len(count)==3:
                ans+=len(s)-r
                count[s[l]]-=1
                if count[s[l]]==0:
                    del count[s[l]]
                l+=1
        return ans