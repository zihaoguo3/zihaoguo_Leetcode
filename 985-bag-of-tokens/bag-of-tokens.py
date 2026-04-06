class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        n=len(tokens)
        start=0
        end=n-1
        points=0
        max_score=0

        while start<=end:
            if power>=tokens[start]:
                points+=1
                power-=tokens[start]
                max_score=max(max_score,points)
                start+=1
            elif points>0 and start<end:
                points-=1
                power+=tokens[end]
                end-=1
            else:
                break
        return max_score

        