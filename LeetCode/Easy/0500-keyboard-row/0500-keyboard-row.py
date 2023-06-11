class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        dic = {}
        for r, seq in enumerate(rows):
            for c in seq:
                dic[c]=r
        
        answer = []
        for word in words:
            low = word.lower()
            cur = dic[low[0]]
            is_failed = False
            for i in range(1, len(low)):
                if cur != dic[low[i]]:
                    is_failed = True
                    break
            
            if not is_failed:
                answer.append(word)
            
            
        return answer