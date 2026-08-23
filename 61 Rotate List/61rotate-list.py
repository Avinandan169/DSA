# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k==0:
            return head
        n=1
        curr=head

        while curr.next:
            curr=curr.next
            n+=1

        curr.next=head

        k=k%n
        if k==0:
            curr.next=None
            return head

        steps=n-k-1
        tail=head

        for i in range(steps):
            tail=tail.next

        head=tail.next
        tail.next=None
        return head
        

