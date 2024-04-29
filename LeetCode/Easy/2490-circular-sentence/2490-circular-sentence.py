class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i in range(len(words)):
            cur_word, next_word = words[i], words[(i+1)%len(words)]
            first, last = next_word[0], cur_word[-1]
            if first != last:
                return False
            
        return True