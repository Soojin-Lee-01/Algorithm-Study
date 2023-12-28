import sys

N = int(sys.stdin.readline().rstrip())
mem = {}
mem[1] = 0
mem[2] = 1
mem[3] = 1
def dp(n): # bottom up 방식
    answer = []
    if n in mem:
        return mem[n]
    for i in range(4, n+1):
        if i % 3 == 0:
            a = dp(i//3) + 1
            answer.append(a)
        if i % 2 == 0:
            b = dp(i//2) + 1
            answer.append(b)
        if i - 1 >= 0:
            c = dp(i-1) + 1
            answer.append(c)
        mem[i] = min(answer)
        answer.clear()
    return mem[n]
print(dp(N))