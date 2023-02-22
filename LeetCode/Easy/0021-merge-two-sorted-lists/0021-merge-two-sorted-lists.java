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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        int i =0, j=0;
        ListNode answer=null;
        ListNode tail =null;
        while(list1 !=null && list2 != null){
            ListNode n;
            if(list1.val < list2.val){
                n = new ListNode(list1.val);
                list1=list1.next;
            } else {
                n = new ListNode(list2.val);
                list2=list2.next;
            }
            
            if(answer==null) {
                answer=new ListNode(n.val);
                tail = answer;
            } else {
                tail.next=n;
                tail=tail.next;
            }
        }
        
        while(list1 != null) {
            if(answer == null){
                answer =new ListNode(list1.val);
                tail=answer;
            } else {
                tail.next=list1;
                tail=tail.next;
            }
            list1=list1.next;
        }
        
        while(list2 != null) {
            if(answer == null){
                answer =new ListNode(list2.val);
                tail=answer;
            } else {
                tail.next=list2;
                tail=tail.next;
            }
            list2=list2.next;
        }
        return answer;
    }
}