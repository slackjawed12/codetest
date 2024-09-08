class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        store = {c:i for i, c in enumerate(order)}
        
        for i in range(len(words)-1):
            cur, n = words[i], words[i+1]
            
            is_before = True
            for x in range(len(cur)):
                if x >= len(n):
                    is_before = False
                    break 

                if store[cur[x]] > store[n[x]]:
                    is_before = False
                    break
                
                if store[cur[x]] < store[n[x]]:
                    is_before = True
                    break
                
            if not is_before:
                return False
            
        return True