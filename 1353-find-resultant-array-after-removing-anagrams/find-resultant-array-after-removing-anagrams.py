class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return words
        
        j=1
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(words[i-1]):
                words[j]=words[i]
                j+=1
                
        return words[:j]
                
        