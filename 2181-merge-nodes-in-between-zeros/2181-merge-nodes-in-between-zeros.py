# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_zero = head
        result = None
        tail = None
        while cur_zero:
            merged = self.sumup(cur_zero.next)
            if not result:
                result = merged
                tail = result
            else:
                tail.next = merged
                tail = merged

            cur_zero = merged.next if merged else None
                
        return result

    def sumup(self, head:Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        cur = head
        total = 0
        while cur and cur.val != 0:
            total += cur.val
            cur = cur.next
        
        if total == 0:
            return None

        merged = ListNode(total, cur)
        return merged