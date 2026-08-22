# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getKthNode(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0,head)
        prev_grp=dummy
        while True:
            kth=self.getKthNode(prev_grp,k)
            if not kth:
                break
            
            next_grp=kth.next

            prev,curr=kth.next,prev_grp.next
            while curr!=next_grp:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=prev_grp.next
            prev_grp.next=kth
            prev_grp=temp
        
        return dummy.next