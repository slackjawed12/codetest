class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        result = "Bob"

        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            result = "Alice" if result == "Bob" else "Bob"

        return result

class Solution2:
    def losingPlayer(self, x: int, y: int) -> str:
        turn = min(x, y//4)
        return "Alice" if turn % 2 else "Bob"