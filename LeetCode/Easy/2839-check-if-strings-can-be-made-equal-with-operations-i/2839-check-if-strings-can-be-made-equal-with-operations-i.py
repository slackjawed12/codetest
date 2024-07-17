class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        store = set([s2])
        store.add(s2[2]+s2[1]+s2[0]+s2[3])
        store.add(s2[0]+s2[3]+s2[2]+s2[1])
        store.add(s2[2]+s2[3]+s2[0]+s2[1])
        return s1 in store
        