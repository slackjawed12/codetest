class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        prefixes = []
        for word in words:
            substr = s[:len(word)]
            if word == substr:
                prefixes.append(word)

        return len(prefixes)