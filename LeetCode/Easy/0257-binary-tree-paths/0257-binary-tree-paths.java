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
    public List<String> binaryTreePaths(TreeNode root, String path, List<String> cur) {
        if(root.left == null && root.right == null){
            cur.add(path.concat(root.val+""));
            return cur;
        } else {
            if(root.left!=null) {
                binaryTreePaths(root.left, path.concat(root.val+"->"), cur);    
            }
            
            if(root.right!=null){
                binaryTreePaths(root.right, path.concat(root.val+"->"), cur);
            }
        }
        
        return cur;
    }
    
    public List<String> binaryTreePaths(TreeNode root) {
        return binaryTreePaths(root, "", new ArrayList<>());    
    }
}