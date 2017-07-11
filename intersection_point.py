"""
https://leetcode.com/problems/intersection-of-two-linked-lists/#/description
Given two linked list.
Find the point of intersection.

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        already_seen = set()

        while headA != None:
            already_seen.add(headA.val)
            headA = headA.next

        while headB != None;
            if headB.val in already_seen:
                return headB.val
            current = current.next

        return 'No intersection'

    def getIntersectionNodeV2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        currentA = headA
        currentB = headB

        while currentA != None:
            while currentB != None:
                if currentA.data == currentB.data:
                    return currentA
                currentB = currentB.next
            currentB = headB
            currentA = currentA.next

        return 'No intersection'
