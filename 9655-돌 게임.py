import sys

# Solution 1 - DP -> 시간 44ms

N = int(sys.stdin.readline())

def stone(n):
    mem = ["NO"] * 1001
    if n == 1 or n == 3:
        mem[n] = "SK"
        print("SK")
    elif n == 2:
        mem[n] = "CY"
        print("CY")
    else:
        for i in range(4, n+1):
            if mem[i-1] == "CY" or mem[i-3] == "CY":
                mem[i] = "SK"
            else:
                mem[i] = "CY"
        print(mem[n])

stone(N)


# Solution 2 -> 시간 40ms

N = int(sys.stdin.readline())

if N % 2  == 0:
    print("CY")
else:
    print("SK")