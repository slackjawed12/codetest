class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        
        return ""
    
    def isPalindrome(self, word:str) -> bool:
        for i in range(len(word)//2):
            if word[i] != word[len(word)-i-1]:
                return False
        
        return True

# reverse
class Solution2:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""