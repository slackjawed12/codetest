# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head, [])
        
    def helper(self, head: Optional[ListNode], l: List[Optional[ListNode]]) -> Optional[ListNode]:
        if head is None:
            return l[len(l)//2]
        
        l.append(head)
        return self.helper(head.next, l)
        
        