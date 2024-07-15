# 241ms
class Solution:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        result = 0
        s1, s2 = self.score(player1), self.score(player2)
        if s1 > s2:
            return 1
        elif s1 < s2:
            return 2
        else:
            return 0
    
    def score(self, arr: list[int]) -> int:
        result = arr[0]
        for i in range(1, len(arr)):
            b, bb = arr[max(i-1,0)], arr[max(i-2,0)]
            if b == 10 or bb == 10:
                result += arr[i] * 2
            else:
                result += arr[i]
        
        return result 

# optimized - 200ms
class Solution2:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        result = 0
        s1, s2 = self.score(player1), self.score(player2)
        if s1 > s2:
            return 1
        elif s1 < s2:
            return 2
        else:
            return 0
    
    def score(self, arr: list[int]) -> int:
        result = 0
        strike = 0
        for i in range(len(arr)):
            if strike == 0:
                result += arr[i]
                if arr[i] == 10:
                    strike = 2
            else:
                result += arr[i] * 2
                if arr[i] == 10:
                    strike = 2
                else:
                    strike -= 1
        
        return result