class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        
        counts = {}
        for rank in ranks:
            if rank not in counts:
                counts[rank] = 1
            else:
                counts[rank] += 1
        
        max_count = max(counts.values())
        if max_count >= 3:
            return "Three of a Kind"
        elif max_count >=2:
            return "Pair"
                
        return "High Card"