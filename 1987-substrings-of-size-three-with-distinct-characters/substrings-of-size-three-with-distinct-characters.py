class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count={}
        l=0
        max_sub=0

        for r, x in enumerate(s):
            count[x]=count.get(x,0)+1
            if (r-l+1)>3:
                count[s[l]]-=1
                if count[s[l]]==0:
                    del count[s[l]]
                l+=1
            if len(count)==3:
                max_sub+=1
        return max_sub
            

        