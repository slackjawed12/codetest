class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        for i in range(len(nums)-k+1):
            sub = nums[i:i+k]
            cnt = defaultdict(int)
            for n in sub:
                cnt[n] += 1
            
            sorted_cnt = sorted(cnt.items(), key=lambda x: (-x[1], -x[0]))
            top_freqs = set([k for k, v in sorted_cnt[:x]])
            result.append(sum([n for n in sub if n in top_freqs]))
        
        return result