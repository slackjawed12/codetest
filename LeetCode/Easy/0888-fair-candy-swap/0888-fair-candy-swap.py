class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        asum = sum(aliceSizes)
        bsum = sum(bobSizes)
        total = asum + bsum
        store = set(bobSizes)
        diff = total//2 - asum
        result = []
        for a in aliceSizes:
            k = diff + a
            if k in store:
                result = [a,k]
                break
        
        return result
        