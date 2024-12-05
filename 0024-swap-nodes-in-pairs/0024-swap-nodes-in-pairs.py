# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        prev, cur = None, head
        while cur:
            next_node = cur.next
            if next_node:
                cur.next = next_node.next
                next_node.next = cur
                if prev:
                    prev.next = next_node

                prev = cur

            if not result:
                result = next_node if next_node else cur

            cur = cur.next
            
        return result
        