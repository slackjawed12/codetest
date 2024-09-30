# first.
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        zero, one = 0, 0
        zcon, ocon = False, False
        result = 0
        for c in s:
            if c == '0':
                if not zcon:
                    zcon, ocon = True, False
                    result += min(zero, one)
                    zero = 0
                zero += 1
            else:
                if not ocon:
                    zcon, ocon = False, True
                    result += min(zero, one)
                    one = 0
                one += 1

        result += min(zero, one)
        
        return result

# second
class Solution2:
    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ans += min(prev, cur)
                prev = cur
                cur = 1
            else:
                cur += 1
        ans += min(prev, cur)
        return ans