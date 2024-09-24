from typing import List
from collections import defaultdict

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        counter = defaultdict(int)
        for c in licensePlate:
            if ord('A') <= ord(c) <= ord('Z'):
                counter[c.lower()] += 1
            elif ord('a') <= ord(c) <= ord('z'): 
                counter[c] += 1
        
        results = []
        for word in words:
            d = defaultdict(int)
            for c in word:
                d[c] += 1
            
            is_answer = True
            for k,v in counter.items():
                if v > (d[k] if k in counter else 0):
                    is_answer = False
                    break
            
            if is_answer:
                results.append(word)
        
        m_len = len(results[0])
        for r in results:
            l = len(r)
            if m_len > l:
                m_len = l

        result = [w for w in results if len(w)==m_len][0]
        return result
