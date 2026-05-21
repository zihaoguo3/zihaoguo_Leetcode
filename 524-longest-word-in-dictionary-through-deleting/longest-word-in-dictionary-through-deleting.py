class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        def is_seq(word,s):
            i,j=0,0

            while i<len(word) and j<len(s):
                if word[i]==s[j]:
                    i+=1
                    j+=1
                else:
                    j+=1
            return i==len(word)

        best=""
        for word in dictionary:
            if is_seq(word,s):
                if len(word)>len(best):
                    best=word
                if len(word)==len(best) and word<best:
                    best=word
        return best

        