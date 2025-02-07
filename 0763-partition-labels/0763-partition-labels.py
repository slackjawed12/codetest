class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = defaultdict(int)
        for i in range(len(s)):
            last_index[s[i]] = i
        
        result = []
        idx = 0
        while idx < len(s):
            partition_end = last_index[s[idx]]
            j = idx
            while j < partition_end:
                if last_index[s[j]] > partition_end:
                    partition_end = last_index[s[j]]
                j += 1
            
            result.append(partition_end - idx + 1)
            idx = partition_end + 1
        
        return result