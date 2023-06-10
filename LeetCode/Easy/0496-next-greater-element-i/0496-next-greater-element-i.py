class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        info={}
        for i, cur in reversed(list(enumerate(nums2))):
            if i == len(nums2)-1:
                info[cur] = -1
            else :
                tail = nums2[i+1]
                if cur < tail:
                    info[cur] = tail
                elif info[tail] == -1:
                    info[cur] = -1
                else:
                    while info[tail] != -1 and cur > info[tail]:
                        tail = info[tail]
                        
                    info[cur] = info[tail]
        
        answer = []
        for i in nums1:
            answer.append(info[i])
        
        return answer
        
            