class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def helper(tiles:str, cur: str, result, visit)->set:
            for i in range(len(tiles)):
                if visit[i]:
                    continue
                temp = cur + tiles[i]
                visit[i] = 1
                result.add(temp)
                result = helper(tiles, temp, result, visit)
                visit[i] = 0

            return result
        
        res = helper(tiles, "", set([]), [0]*len(tiles))
        return len(res)