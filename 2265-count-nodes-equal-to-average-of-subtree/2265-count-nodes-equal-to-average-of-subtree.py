# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = self.helper(root)
        print(result)
        return result[0]
    
    def helper(self, root: TreeNode):
        if not root.left and not root.right:
            return (1, root.val, 1)
        elif not root.right:
            la, ls, lc = self.helper(root.left)
            cur_avg = (ls+root.val) // (lc+1)
            return (la+1 if cur_avg == root.val else la, root.val+ls, lc+1)
        elif not root.left:
            ra, rs, rc = self.helper(root.right)
            cur_avg = (rs+root.val) // (rc+1)
            return (ra+1 if cur_avg == root.val else ra, root.val+rs, rc+1)

        la, ls, lc = self.helper(root.left)
        ra, rs, rc = self.helper(root.right)
        cur_avg = (ls+rs+root.val) // (lc+rc+1)
        return (la+ra+1 if cur_avg == root.val else la+ra, root.val+rs+ls, lc+rc+1)

