class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        answer, count, index = False, 0, 0
        for i, c in enumerate(word):
            if ord('A') <= ord(c) <= ord('Z'):
                count += 1
                index = i
        
        if (count == len(word)) or (count == 1 and index == 0) or count == 0:
            answer = True
        
        return answer