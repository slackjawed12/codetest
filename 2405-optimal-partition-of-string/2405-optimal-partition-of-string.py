class Solution:
    def partitionString(self, s: str) -> int:
        result = 0
        store = set()
        for c in s:
            if c in store:
                store = set()
                result += 1

            store.add(c)

        if store:
            result += 1
        
        return result