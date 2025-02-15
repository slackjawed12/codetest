class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = defaultdict(int)
        for domain in cpdomains:
            cnt, url = domain.split()
            arr = url.split('.')
            cur = ''
            while arr:
                part = arr.pop()
                if not cur:
                    cur =part
                else:
                    cur = part + '.' + cur
                store[cur] += int(cnt)
                
        return [" ".join([str(v), k]) for k, v in store.items()]