class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        cur = s
        while True:
            find = False
            for i in range(len(cur)-len(part)+1):
                if cur[i:i+len(part)] == part:
                    cur = cur[:i]+cur[i+len(part):]
                    find = True
                    break
            
            if not find:
                break

        return cur