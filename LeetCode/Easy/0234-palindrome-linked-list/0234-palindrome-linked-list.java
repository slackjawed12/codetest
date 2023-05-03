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
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        
        while(fast!=null){
            fast=fast.next;
            if(fast!=null) {
                fast=fast.next;
                slow=slow.next;
            }
        }
        
        ListNode tail = slow.next;
        ListNode prev = slow;
        prev.next=null;
        while(tail!=null){
            ListNode temp = tail;
            tail=tail.next;
            temp.next=prev;
            prev=temp;
        }
        
        tail=prev;
        while(tail!=null){
            if(head.val!=tail.val){
                return false;
            }
            
            head=head.next;
            tail=tail.next;
        }
        
        return true;
    }
}