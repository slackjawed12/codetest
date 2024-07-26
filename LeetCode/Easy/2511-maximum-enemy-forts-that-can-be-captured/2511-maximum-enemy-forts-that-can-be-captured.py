class Solution:
    def captureForts(self, forts: list[int]) -> int:
        result = 0
        length = len(forts)
        last_empty,last_my = None,None
        for i, cur in enumerate(forts):
            if cur == 1:
                # here is my fort
                if last_empty is not None:
                    # there is a empty fort before this fort
                    if last_my is None or last_my < last_empty:
                        result = max(result, i - last_empty - 1)

                last_my = i
            if cur == -1:
                if last_my is not None:
                    # there is a my fort before this empty
                    if last_empty is None or last_empty < last_my:
                        # and not screened by before empty
                        result = max(result, i - last_my - 1)
                        last_empty = i
                        
                last_empty = i
            
        return result