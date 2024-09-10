from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True
        elif root.left is None and root.right is not None:
            return root.val == root.right.val and self.isUnivalTree(root.right)
        elif root.right is None and root.left is not None:
            return root.val == root.left.val and self.isUnivalTree(root.left)

        if root.left is not None and root.right is not None:
            if root.val != root.left.val or root.val != root.right.val:
              return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)