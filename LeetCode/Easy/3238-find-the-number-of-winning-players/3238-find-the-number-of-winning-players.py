from collections import defaultdict

class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        p = dict()
        for pair in pick:
            if pair[0] not in p:
                p[pair[0]]= [pair[1]]
            else:
                p[pair[0]].append(pair[1])
        
        result = 0
        for key, value in p.items():
            if self.is_winner(key, value):
                result += 1

        return result
    
    def is_winner(self, player:int, colors:list[int]) -> bool:
        cnts = defaultdict(int)
        
        for c in colors:
            cnts[c] += 1
            if cnts[c] >= player + 1:
                return True
                
        return False
            