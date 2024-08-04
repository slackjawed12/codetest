# 413ms, 36.3MB
import heapq
class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        acc = []
        heapq.heapify(acc)
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                heapq.heappush(acc, cur+nums[j])
                cur += nums[j]
        
        cnt = 0
        result = 0
        while acc:
            cnt += 1
            n = heapq.heappop(acc)
            if left <= cnt <= right:
                result += n % (10**9 +7)
                result %= 10**9 + 7
            
            if cnt == right:
                break

        return result

# 65ms, 16.9MB
class SolutionV2:
    s1:list[int]
    s2:list[int]
    n: int
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        MODULI = 10 ** 9 + 7
        
        self.init(nums)
        
        val_left = self.index_to_value(left)
        val_right = self.index_to_value(right)
        
        # Case 1: If two values are equal, then the sorted subarray sums are constant between the indices left and right inclusive. 
        # Calculate the result as val_left * (right - left + 1).
        if val_left == val_right:
            return val_left * (right - left + 1) % MODULI
        
        # Case 2: val_left < val_right
        # calculate the index range (left_exc, right_exc] of the sorted subarray sums that correspond to the values 
        # between val_left and val_right
        left_exc = self.count_subarr_limit_of(val_left)
        right_exc = self.count_subarr_limit_of(val_right - 1)
        ret = (val_left * (left_exc - (left - 1)) + val_right * (right - right_exc)) % MODULI
        
        # additional process
        if val_left + 1 <= val_right - 1:
            head_l = head_r = tail = 0
            
            while self.s1[tail] < val_left + 1 and tail <= n:
                tail += 1
            
            while tail <= n:
                # find the least head_l such that sum(nums[head_l:tail]) <= val_right - 1
                while self.s1[tail] - self.s1[head_l] > val_right - 1:
                    head_l += 1
                
                # find the greatest head_r such that sum(nums[head_r:tail]) >= val_left + 1
                while self.s1[tail] - self.s1[head_r + 1] >= val_left + 1:
                    head_r += 1
                
                if head_l <= head_r:
                    ret = (ret + self.s1[tail] * (head_r - head_l + 1) - (self.s2[head_r + 1] - self.s2[head_l])) % MODULI
                
                tail += 1
        
        return ret

    def init(self, nums):
        self.n = len(nums)

        # first order cumulative sum
        self.s1 = [0]
        for i in nums:
            self.s1.append(self.s1[-1] + i)
        
        # second order cumulative sum
        self.s2 = [0]
        for i in self.s1:
            self.s2.append(self.s2[-1] + i)


    # returns the ind-th smallest non-empty subarray sum.
    # Binary Search -> O(n * log(sum(nums)))
    # nums[i]의 범위가 1부터 100이므로 효율적임
    def index_to_value(self, ind: int) -> int:
        min_ = 0
        max_ = self.s1[self.n]
        while min_ < max_:
            mid = min_ + ((max_ - min_) >> 1)
            if self.count_subarr_limit_of(mid) < ind:
                min_ = mid + 1
            else:
                max_ = mid
        
        return min_

    # 누적합 배열을 이용해서, 합이 최대 limit인 부분배열의 개수를 구한다.
    # ex) [0,1,3,6,10] -> nvals_le(5) = 6
    # Two Pointer 활용 -> O(n)
    def count_subarr_limit_of(self, limit: int) -> int:
        if limit <= 0:
            return 0
        
        ret = 0
        lptr = 0
        for rptr in range(1, self.n + 1):
            while self.s1[rptr] - self.s1[lptr] > limit:
                lptr += 1
            ret += rptr - lptr
        
        return ret