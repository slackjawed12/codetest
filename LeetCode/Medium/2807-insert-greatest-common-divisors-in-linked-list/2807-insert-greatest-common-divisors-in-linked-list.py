# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head, head)
        
    def helper(self, head:Optional[ListNode], result: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return result
        
        if head.next is None:
            return result
        
        bef = head.next
        n = ListNode(self.gcd(head.val, head.next.val), head.next)
        head.next = n
        
        return self.helper(bef, result)
    
    def gcd(self, a:int, b:int) -> int:
        if b == 0:
            return a
        
        return self.gcd(b, a%b)