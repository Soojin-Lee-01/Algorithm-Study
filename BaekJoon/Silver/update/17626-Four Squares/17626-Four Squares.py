import math
import sys

n = int(sys.stdin.readline())
dp = [0, 1]

for i in range(2, n + 1):
    minValue = 4
    for j in range(1, int(math.sqrt(i)) + 1):
        minValue = min(minValue, dp[i - j ** 2])
    dp.append(minValue + 1)

print(dp[n])

