class Solution:
    digitMap = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs",8:"tuv",9:"wxyz"}
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        return self.combiHelper(digits, 0, [], [])
    
    def combiHelper(self, digits, pos, current, result):
        if pos == len(digits):
            result.append("".join(current))
            return result
        
        letters = self.digitMap[int(digits[pos])]
        for c in letters:
            current.append(c)
            self.combiHelper(digits, pos + 1, current, result) 
            current.pop()

        return result
  
class SolutionV2:
    def letterCombinations(self, digits: str) -> list[str]:
      if not digits:
          return []
      
      phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
      res = []
      
      def backtrack(combination, next_digits):
          if not next_digits:
              res.append(combination)
              return
          
          for letter in phone[next_digits[0]]:
              backtrack(combination + letter, next_digits[1:])
      
      backtrack("", digits)
      return res