class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        cnt = 0
        for i in range(len(word)):
            if word[i] not in vowels:
                continue

            for j in range(i+4, len(word)):
                sub = word[i:j+1]
                if set(sub) == vowels:
                    cnt += 1

        return cnt