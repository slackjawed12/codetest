from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode()
        prev, cur = None, result
        one, two = l1,l2
        while one or two:
            total = (one.val if one else 0) + (two.val if two else 0) + carry
            digit, carry = (total-10, 1) if total >= 10 else (total, 0)
            cur.val = digit
            cur.next = ListNode()
            prev = cur
            cur = cur.next
            one, two = (one.next if one else None), (two.next if two else None)
        
        if carry:
            cur.val = carry
        elif prev is not None:
            prev.next = None

        return result
            