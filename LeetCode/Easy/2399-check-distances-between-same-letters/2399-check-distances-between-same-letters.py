class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        alphabets = {c:[] for c in s}
        for i in range(len(s)):
            alphabets[s[i]].append(i)

        for key, val in alphabets.items():
            index = ord(key) - ord('a')
            if distance[index] != val[1] - val[0] - 1:
                return False

        return True