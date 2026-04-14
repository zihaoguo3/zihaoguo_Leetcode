class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        n=len(tokens)
        tokens.sort()
        max_point=0
        point=0
        left=0
        right=n-1

        while left<=right:
            if tokens[left]<=power:
                power-=tokens[left]
                point+=1
                max_point=max(max_point,point)
                left+=1
            elif point>0:
                power+=tokens[right]
                point-=1
                right-=1
            else:
                break
        return max_point