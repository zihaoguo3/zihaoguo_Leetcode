class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n


        fv, sv = 0,1

        for i in range(n-2):
            temp=fv+sv
            fv=sv
            sv=temp
        return fv+sv


    
        
        