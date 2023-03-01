/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {

    public ListNode deleteDuplicates(ListNode head) {
        ListNode ex = head;
        ListNode n = head;
        while(n!=null){
            if(ex.val!=n.val) {
                ex.next =n;
                ex = n;
            }
            n=n.next;
        }
        if(ex!=null) ex.next=n;
        return head;
    }
}