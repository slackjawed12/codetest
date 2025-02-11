class Solution:
    def minSwaps(self, s: str) -> int:
        stack_size = 0
        for ch in s:
            # If character is opening bracket, increment the stack size.
            if ch == "[":
                stack_size += 1
            else:
                # If the character is closing bracket, and we have an opening bracket, decrease
                # the stack size.
                if stack_size > 0:
                    stack_size -= 1

        # for each optimized balancing(']' and '['), unbalance is decreased by 2
        # therefore total swap count is (size+1)//2
        # ex) ]]][[[ -> unbalance pair is 3
        # after swap index 0, 5 -> unbalance pair is 1 (3-2)
        # and then swap index 2, 3 -> unbalance pair is 0 (1-0)
        # total swap count = 2 = (3+1)//2
        return (stack_size + 1) // 2