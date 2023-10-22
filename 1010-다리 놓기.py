import sys

number = int(sys.stdin.readline())

def dp(num):
    arr = {}
    if num == 0 or num == 1:
        arr[num] = 1
    else:
        arr[num] = num * dp(num-1)
    return arr[num]


for i in range(number):
    n, r = map(int, sys.stdin.readline().split())
    ans = dp(r) // (dp(n) * dp(r - n))
    print(ans)


"""
조합을 구하는 문제! - dp
C(n, r) = n! / r! * (n - r)!
"""



