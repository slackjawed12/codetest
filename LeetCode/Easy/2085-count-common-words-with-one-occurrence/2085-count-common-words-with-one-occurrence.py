class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        dict1 = self.initCounter(words1)
        dict2 = self.initCounter(words2)
        result = 0
        for k, v in dict1.items():
            if v == 1 and k in dict2 and dict2[k] == 1:
                result += 1
        return result
    
    def initCounter(self, arr:list[str]) -> dict:
        result = {}
        for elem in arr:
            if elem not in result:
                result[elem] = 1
            else:
                result[elem] += 1
        
        return result
            