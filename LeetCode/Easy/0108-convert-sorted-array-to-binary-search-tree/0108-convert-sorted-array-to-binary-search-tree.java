/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode make(int[] nums, int low, int high){
        if(low > high) {
            return null;
        } else {
            int mid =(low+high)/2;
            TreeNode l = make(nums, low, mid-1);
            TreeNode r = make(nums, mid+1, high);
            return new TreeNode(nums[mid], l, r);
        }
    }
    public TreeNode sortedArrayToBST(int[] nums) {
        return make(nums, 0, nums.length-1);
    }
}