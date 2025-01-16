# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l = list1
        for i in range(a-1):
            l = l.next
        
        r = list1
        for i in range(b):
            r = r.next
        
        l.next = list2
        end = list2
        while end.next:
            end = end.next
        
        end.next = r.next
        return list1

        