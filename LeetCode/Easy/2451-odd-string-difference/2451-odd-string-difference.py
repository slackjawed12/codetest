class Solution:
    def oddString(self, words: list[str]) -> str:
        diffs = {}
        for word in words:
            diff = self.difference(word)
            key = "".join(str(diff))
            if key not in diffs:
                diffs[key] = [1, word]
            else:
                diffs[key][0] += 1
        
        vals = list(diffs.values())
        return vals[0][1] if vals[0][0] == 1 else vals[1][1]

    def difference(self, word:str)-> list[int]:
        result = []
        for i in range(1,len(word)):
            result.append(ord(word[i])-ord(word[i-1]))
            
        return result

