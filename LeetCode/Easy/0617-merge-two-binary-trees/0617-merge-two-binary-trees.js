/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */
var mergeTrees = function(root1, root2) {
    if(!root1 && !root2) {
        return null;
    } else if (!root1 && root2) {
        return new TreeNode(root2.val, mergeTrees(null, root2.left), mergeTrees(null, root2.right));
    } else if(root1 && !root2){
        return new TreeNode(root1.val, mergeTrees(root1.left, null), mergeTrees(root1.right, null)); 
    } else {
        return new TreeNode(root1.val + root2.val, mergeTrees(root1.left, root2.left),
                           mergeTrees(root1.right, root2.right));    
    }
};