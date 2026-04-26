class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count=1
        left=0

        for i in range(1,len(prices)):
            while prices[i]+1!=prices[i-1] and left<i:
                left+=1
            
            count+=(i-left+1)
        return count
            