"""
RGB거리
- DP로 풀이!
- 시간복잡도 : O(n)
"""
n = int(input())

nums = []

for _ in range(n):
    data = list(map(int, input().split()))
    nums.append(data)

def dp(nums):
    for i in range(1, n):
        nums[i][0] = min(nums[i-1][1], nums[i-1][2]) + nums[i][0]
        nums[i][1] = min(nums[i-1][0], nums[i-1][2]) + nums[i][1]
        nums[i][2] = min(nums[i-1][0], nums[i-1][1]) + nums[i][2]

    return nums

print(min(dp(nums)[n-1]))
