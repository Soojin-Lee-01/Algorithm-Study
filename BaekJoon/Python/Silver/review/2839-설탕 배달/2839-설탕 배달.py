import sys

N = int(sys.stdin.readline())

def sugar(n):
    dp = [-1] * 5001
    dp[3] = 1
    dp[4] = -1
    dp[5] = 1
    for i in range(6, n+1):
        if dp[i - 5] != -1:
            dp[i] = dp[5] + dp[i - 5]
        else:
            if i % 3 == 0:
                dp[i] = i // 3

    return dp[n]

print(sugar(N))