/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head==null) return false;
        
        ListNode s = head;
        ListNode f = head;
        s=head.next;
        f=head.next;
        if(f!=null){
            f=f.next;
        }
        
        while(f!=null && s!=f){
            s=s.next;
            f=f.next;
            if (f!=null) {
                f=f.next;
            } else {
                return false;   
            }
        }
        
        if(s==f && f!=null) return true;
        else return false;
    }
}