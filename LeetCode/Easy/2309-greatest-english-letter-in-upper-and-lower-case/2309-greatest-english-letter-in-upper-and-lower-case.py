class Solution:
    def greatestLetter(self, s: str) -> str:
        store = set(s)
        lowers = [c for c in store if ord('a') <= ord(c) <= ord('z')]
        lowers.sort(reverse=True)
        for l in lowers:
            if l.upper() in store:
                return l.upper()

        return ""