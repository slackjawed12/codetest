class Solution:
    def minimumChairs(self, s: str) -> int:
        st = []
        result = 0
        for c in s:
            if c == 'E':
                st.append(c)
                result = max(len(st), result)
            else:
                st.pop()

        return result