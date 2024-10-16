class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        counter = defaultdict(int)
        cur =""
        for c in paragraph:
            if ord('A') <= ord(c) <= ord('Z'):
                cur += c.lower()
            elif ord('a') <= ord(c) <= ord('z'):
                cur += c
            else:
                if cur not in ban and len(cur) >= 1:
                    counter[cur] += 1
                cur = ""

        if cur not in ban and len(cur) >= 1:
            counter[cur] += 1
            
        result, mx = "", 0
        for k,v in counter.items():
            if v > mx:
                result = k
                mx = v

        return result