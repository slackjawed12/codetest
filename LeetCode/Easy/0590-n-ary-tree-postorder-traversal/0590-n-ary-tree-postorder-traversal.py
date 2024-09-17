from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

# recursive solution
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        return self.postorderHelper(root, [])
        
    def postorderHelper(self, root:'Node', result:List[int]) -> List[int]:
        if root is None:
            return result
        else:
            if not root.children:
                if root.val:
                  result.append(root.val)
            else:    
                for c in root.children:
                    result = self.postorderHelper(c, result)
                
                if root.val: 
                  result.append(root.val)
        
        return result

# iterative solution
class Solution2:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
            
        res, stack = [], [root]
        
        while stack:
            temp = stack.pop()
            res.insert(0, temp.val)  # Insert at the beginning to reverse postorder sequence
            if temp.children:
              stack.extend(temp.children)
        
        return res