class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = deque([])
        while deck:
            if result:
                last = result.pop()
                result.appendleft(last)
            
            result.appendleft(deck.pop())
        
        return list(result)
        