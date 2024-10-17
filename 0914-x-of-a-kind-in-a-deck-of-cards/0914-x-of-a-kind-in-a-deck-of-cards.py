class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        store = defaultdict(int)
        for n in deck:
            store[n] += 1
        
        freq = list(set(store.values()))
        gcp = self.gcp(freq[0], freq[1]) if len(freq) >= 2 else freq[0]
        for i in range(2, len(freq)-1):
            gcp = self.gcp(gcp, freq[i])

        return gcp >= 2
    
    def gcp(self, a:int, b:int) -> int:
        if b==0:
            return a
        
        return self.gcp(b, a%b)
        