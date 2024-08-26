def solution(n):
    mem = {}
    mem[1] = 1
    mem[2] = 2
    for i in range(3, n+1):
        mem[i] = (mem[i-1] + mem[i-2]) % 1234567

    return mem[n]

