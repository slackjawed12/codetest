class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        result = 0

        store = set(word)
        for a in 'abcdefghijklmnopqrstuvwxyz':
            if a in store and a.upper() in store:
                result += 1

        return result