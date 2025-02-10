class Solution:
    def countVowelStrings(self, n: int) -> int:

        return (4+n)*(3+n)*(2+n)*(1+n)//24