from collections import defaultdict
class Solution:
    def digitCount(self, num: str) -> bool:
        store = defaultdict(int)
        for c in num:
            store[c] += 1
        
        print(store)
        for i, c in enumerate(num):
            if store[str(i)] != int(c):
                return False
                
        return True