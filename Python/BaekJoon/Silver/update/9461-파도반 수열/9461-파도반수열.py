"""
DP로 풀이
시간복잡도 : O(N)
"""

N = int(input())

mem = [0] * 101
mem[0] = 1
mem[1] = 1
mem[2] = 1
mem[3] = 2
mem[4] = 2
def dp():
    for i in range(5, 101):
        mem[i] = mem[i-1] + mem[i-5]

dp()

for _ in range(N):
    num = int(input())
    print(mem[num-1])
