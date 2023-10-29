import sys

# Solution 1
N = int(sys.stdin.readline())

bag = 0

while N >= 0:
    if N % 5 == 0:
        bag += N // 5
        print(bag)
        break
    N -= 3
    bag += 1
else:
    print(-1)


# Solution 2 - DP
N = int(sys.stdin.readline())

dp = [-1] * (N+1)

if N >= 3:
    dp[3] = 1
if N >= 5:
    dp[5] = 1
for i in range(6, N + 1):
    if dp[i-3] < 0 and dp[i-5] < 0:
        dp[i] = -1
    elif dp[i-3] > 0 and dp[i-5] > 0:
        dp[i] = 1 + min(dp[i-3], dp[i-5])
    else:
        dp[i] = 1 + max(dp[i-3], dp[i-5])

print(dp[N])


