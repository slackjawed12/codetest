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
    public boolean hasPathSum(TreeNode root, int targetSum, int inter){
        if(root.left==null && root.right==null) {
            return inter+root.val==targetSum;
        } else if(root.left==null){
            return hasPathSum(root.right, targetSum, inter+root.val);
        } else if(root.right==null){
            return hasPathSum(root.left, targetSum, inter+root.val);
        } else {
            return hasPathSum(root.left, targetSum, inter+root.val) ||
                hasPathSum(root.right, targetSum, inter+root.val);
        }
    }
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root==null) return false;
        return hasPathSum(root, targetSum, 0);
    }
}