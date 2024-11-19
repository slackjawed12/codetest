# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)
    
    def helper(self, root: Optional[TreeNode], result: int) -> int:
        if root is None:
            return result
        
        result += 1
        result = self.helper(root.left, result)
        result = self.helper(root.right, result)
        return result
        

# optimal approach
# using the  Height property of COmplete tree to get TC= O(h)
class SolutionV2:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def lefttreenodes(node):
            count = 0
            while node:
                node  = node.left
                count += 1
            return count 
        def righttreenodes(node):
            count = 0
            while node:
                node = node.right
                count += 1
            return count 
        
        if root is None:
            return 0

        lnodes = lefttreenodes(root)
        rnodes = righttreenodes(root)
        if lnodes == rnodes:
            return 2**lnodes - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)