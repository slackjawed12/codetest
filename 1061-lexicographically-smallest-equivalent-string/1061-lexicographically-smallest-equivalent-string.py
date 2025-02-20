class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {c:c for c in 'abcdefghijklmnopqrstuvwxyz'}
        def union(parent, a, b):
            a = getparent(parent, a)
            b = getparent(parent, b)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b
            
        def find(parent, a, b):
            a = getparent(parent, a)
            b = getparent(parent, b)
            if a == b:
                return 1
            else:
                return 0
        
        def getparent(parent, x):
            if parent[x] == x:
                return x
            parent[x] = getparent(parent, parent[x])
            return parent[x]

        for i in range(len(s1)):
            union(parent, s1[i], s2[i])

        return "".join([getparent(parent,c) for c in baseStr])
            
            