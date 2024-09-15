from typing import List, Optional

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.maxDepthHelper(root, 0)
    
    def maxDepthHelper(self, root: 'Node', depth: int) -> int:
        if root is None:
            return depth
        
        result = depth + 1

        if root.children is None:
            return result

        for c in root.children:
            
            result = max(result, self.maxDepthHelper(c, depth+1))

        return result