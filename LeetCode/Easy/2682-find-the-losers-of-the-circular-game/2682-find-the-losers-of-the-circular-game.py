class Solution:
    def circularGameLosers(self, n: int, k: int) -> list[int]:
        receive_counts = {i:0 for i in range(1, n+1)}
        cur_player = 1
        receive_counts[cur_player] += 1
        multiple = k
        while receive_counts[cur_player] != 2:
            next_player = cur_player
            for i in range(multiple):
                if next_player == n:
                    next_player = 1
                else:
                    next_player += 1

            cur_player = next_player
            multiple += k
            receive_counts[cur_player] += 1
        
        return [key for key, val in receive_counts.items() if val == 0]
    
class Solution2:
    def circularGameLosers(self, n: int, k: int) -> list[int]:
        ans=[0]
        m=k
        while True:
            if (ans[-1]+m)%n not in ans:
                ans.append((ans[-1]+m)%n)
                m=m+k

            else:
                break

        return [i+1 for i in range(n) if i not in ans]