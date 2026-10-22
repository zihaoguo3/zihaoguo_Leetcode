# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummyHead=ListNode(0)
        curr = dummyHead
        carry=0
        while l1 != None or l2!=None or carry!=0:
            l1_val=l1.val if l1 else 0
            l2_val=l2.val if l2 else 0
            colsum=l1_val+l2_val+carry
            carry=colsum//10
            newNode=ListNode(colsum%10)
            curr.next=newNode
            curr=newNode
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummyHead.next

        
        