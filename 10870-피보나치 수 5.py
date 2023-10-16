import sys

n = int(sys.stdin.readline())

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    result = fibo(n-1) + fibo(n-2)

    return result

print(fibo(n))

# 시간복잡도 O(2^n)