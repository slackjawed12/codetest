from typing import List, Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        result = self.cousinHelper(root, x, y, 0, -1, [])
        return result[0][0] != result[1][0] and result[0][1] == result[1][1]

    def cousinHelper(self, root: Optional[TreeNode], x:int, y:int, depth:int, parent:int, result:List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if root is None:
            return result

        if root.val == x or root.val == y:
            result.append((parent, depth))

        if root.left:
            result = self.cousinHelper(root.left, x, y, depth+1, root.val, result)
        if root.right:
            result = self.cousinHelper(root.right, x, y, depth+1, root.val, result)
        
        return result
