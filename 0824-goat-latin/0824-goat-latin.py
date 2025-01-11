class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result = []
        vowels=set('aeiouAEIOU')
        for i, word in enumerate(sentence.split()):
            temp = ''
            if word[0] in vowels:
                temp = word + 'ma'
            else:
                temp = word[1:]
                temp = temp + word[0]
                temp = temp + 'ma'
            
            temp = temp + 'a'*(i+1)
            result.append(temp)
        
        return " ".join(result)
            
            

            