class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        q = deque(s)
        for i in range(len(s)):
            if "".join(q) == goal:
                return True
                
            q.append(q.popleft())
        
        return False