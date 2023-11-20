import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

mem = {}
def fibo(n):
    if n == 0:
        mem[n] = 0
    elif n == 1 or n == 2:
        mem[n] = 1
    else:
        mem[n] = fibo(n-1) + fibo(n-2)

    return mem[n]

print(fibo(n))