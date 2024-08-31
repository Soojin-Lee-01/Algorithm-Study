from collections import deque

def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    
    for y in range(n):
        for x in range(m):
            if [x+1, y+1] in puddles:
                dp[y][x] = 0
            else:
                if x > 0:
                    dp[y][x] += dp[y][x-1]
                if y > 0:
                    dp[y][x] += dp[y-1][x]
    
    return dp[-1][-1] % 1000000007
