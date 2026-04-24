class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        left, right=0,0
        l1,l2=len(word1),len(word2)
        ans=""

        while left<l1 and right<l2:
            ans+=word1[left]
            left+=1
            ans+=word2[right]
            right+=1
        
        while left<l1:
            ans+=word1[left]
            left+=1
        while right<l2:
            ans+=word2[right]
            right+=1
        return ans

            



