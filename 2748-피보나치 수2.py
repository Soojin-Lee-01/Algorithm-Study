import sys

n = int(sys.stdin.readline())

memo = {}
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

print(fibo(n))


# 시간복잡도 O(n)