import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().strip().split()))
nums.sort()

P, S = sum(nums[:len(nums)//2]), sum(nums[len(nums)//2:])

print(P, S)