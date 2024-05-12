class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
       store = set(range(left, right+1))
       for cover in ranges:
            for i in range(cover[0], cover[1]+1):
                if i in store:
                    store.remove(i)
                    
       return len(store) == 0