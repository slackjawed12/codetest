/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function getDecimalValue(head: ListNode | null): number {
    return getDecimalValueHelper(head, 0);
};

function getDecimalValueHelper(head: ListNode | null, result: number): number {
    if(head===null) {
        return result;
    }
    
    return getDecimalValueHelper(head.next, (result << 1) | head.val);
}