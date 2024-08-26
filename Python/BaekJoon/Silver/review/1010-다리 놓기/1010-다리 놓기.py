# math 라이브러리로 해결 - 1

import sys
import math

sys.setrecursionlimit(10**8)

T = int(sys.stdin.readline())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    result = math.factorial(b) // (math.factorial(a) * math.factorial(b-a))
    print(result)

# DP를 이용하여 해결 - 2

import sys

T = int(sys.stdin.readline())

def dp(n):
    mem = {}
    if n in mem:
        return mem[n]
    elif n == 0 or n == 1:
        mem[n] = 1
    else:
        mem[n] = n * dp(n - 1)
    return mem[n]

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())

    ans = dp(b) // (dp(b-a) * dp(a))
    print(ans)