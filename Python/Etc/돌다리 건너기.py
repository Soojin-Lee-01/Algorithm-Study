num = int(input())

mem = [0 for _ in range(35)]
mem[1] = 1
mem[2] = 2
def dp(n):
    if n in mem:
        return mem[n]
    else:
        if n == 1 or n == 2:
            return mem[n]
        for i in range(3, n+1):
            mem[i] = mem[i-1] + mem[i-2]

    return mem[n]

print(dp(num))
