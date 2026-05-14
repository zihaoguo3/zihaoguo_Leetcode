class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1=[]
        stack2=[]

        for each in s:
            if each=='#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(each)
        for each in t:
            if each=='#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(each)
        return stack1==stack2