class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[tuple[int, int]]:
        store = {v:w for v, w in items1}
        for v, w in items2:
            if v not in store:
                store[v] = w
            else:
                store[v] += w
                
        result = sorted(store.items(), key=lambda x:x[0])
        return result
        