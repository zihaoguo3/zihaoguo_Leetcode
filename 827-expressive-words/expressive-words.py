class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        ans=0
        def is_stretchy(word):
            i,j=0,0
            while i<len(s) and j<len(word):
                if s[i]!=word[j]:
                    return False
                
                char=s[i]
                len_s=0
                while i<len(s) and char==s[i]:
                    len_s+=1
                    i+=1
                
                len_w=0
                while j<len(word) and char==word[j]:
                    len_w+=1
                    j+=1
                
                if len_w>len_s or (len_w<len_s and len_s<3):
                    return False
            return i==len(s) and j==len(word)

        for word in words:
            if is_stretchy(word):
                ans+=1
        return ans






        