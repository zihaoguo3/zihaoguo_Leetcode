class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count1={}
        count2={}

        for i, x in enumerate(s1):
            count1[x]=count1.get(x,0)+1
        
        n = len(s1)

        for i, x in enumerate(s2):
            count2[x]=count2.get(x,0)+1
            if i>=n:
                del_value=s2[i-n]
                count2[del_value]-=1
                if count2[del_value]==0:
                    del count2[del_value]
            if count1==count2:
                return True
        return False
            

