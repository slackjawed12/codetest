from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# iterative
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sub = self.search(subRoot, [])
        r = self.search(root, [])
        for i in range(len(sub), len(r)+1):
            s = r[i-len(sub):i]
            if s == sub:
                return True

        return False

    def search(self, root: Optional[TreeNode], result: List[int | None]) -> List[int | None]:
        if root is None:
            result.append(None)
            return result
        
        result.append(root.val)
        result = self.search(root.left, result)
        result = self.search(root.right, result)
        return result

# recursive
class SolutionV2:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSametree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSametree(self, t, s):
        if not t and not s:
            return True
        if not t or not s or t.val != s.val:
            return False
        return self.isSametree(t.left, s.left) and self.isSametree(t.right, s.right)
