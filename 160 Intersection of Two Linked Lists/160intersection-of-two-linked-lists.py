# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        listA=headA
        listB=headB
        while listA!=listB:
            listA=listA.next if listA else headB
            listB=listB.next if listB else headA
        
        return listA