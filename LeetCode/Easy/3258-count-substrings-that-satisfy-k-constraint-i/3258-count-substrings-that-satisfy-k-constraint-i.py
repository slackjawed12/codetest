# brute force with cache
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        store = set()
        result = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub in store:
                    result += 1
                    continue

                zero, one = 0, 0
                for c in sub:
                    if c == '1':
                        one += 1
                    else:
                        zero += 1

                if zero <= k or one <= k:
                    result += 1
                    store.add(sub)

        return result

# sliding window. caterpillar technique
# Time complexity: O(n)
# Space complexity: O(1)
class Solution2:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        result = 0
        left = 0
        one = 0
        for right in range(len(s)):
            one += 1 if s[right] == '1' else 0

            while one > k and right-left+1-one > k:
                one -= 1 if s[left] == '1' else 0
                left += 1
            
            # 이제 left ~ right 까지 right 위치를 포함하는 모든 substring은 조건을 만족한다.
            result += right - left + 1

        return result