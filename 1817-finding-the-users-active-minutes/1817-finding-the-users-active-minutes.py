class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        store = {}
        for user, time in logs:
            if user in store:
                store[user].add(time)
            else:
                store[user] = set([time])
        
        result = [0]*k
        for k, v in store.items():
            result[len(v)-1] += 1

        return result
            