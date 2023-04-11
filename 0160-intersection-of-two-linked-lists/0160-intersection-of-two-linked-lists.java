/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int cntA = 0;
        int cntB = 0;
        ListNode startA = headA;
        ListNode startB = headB;
        
        while(headA != null) {
            headA = headA.next;
            cntA++;
        }
        
        while(headB != null) {
            headB = headB.next;
            cntB++;
        }
        
        headA = startA;
        headB = startB;
        
        if(cntB > cntA) {
            while (cntB != cntA) {
                headB = headB.next;
                cntB--;
            }
        } else {
            while (cntA != cntB) {
                headA = headA.next;
                cntA--;
            }
        }
        
        while(headA != headB && headA != null && headB != null){
            headA = headA.next;
            headB = headB.next;
        }
        
        return headA;
    }
}