class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        prev = list(words[0])
        prev.sort()
        for i in range(1,len(words)):
            cur = list(words[i])
            cur.sort()
            if prev==cur:
                words[i] = '-1'
            else:
                prev= list(words[i])
                prev.sort()
        
        return [word for word in words if word != '-1']