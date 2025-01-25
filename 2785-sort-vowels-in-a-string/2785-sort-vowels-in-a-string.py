class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        store = defaultdict(int)
        for c in s:
            if c in vowels:
                store[c] += 1
            
        result = []
        sorted_store = deque(sorted(map(lambda x:list(x), store.items()), key=lambda x:x[0]))
        for c in s:
            if c not in vowels:
                result.append(c)
            else:
                result.append(sorted_store[0][0])
                sorted_store[0][1] -= 1
                if not sorted_store[0][1]:
                    sorted_store.popleft()

        return "".join(result)
