"""
시간 복잡도 : O(N)
"""

N, M = map(int, input().split())

data = list(map(int, input().split()))

mem = [0] * (len(data) + 1)
mem[0] = data[0]
for i in range(1, len(data)):
    mem[i] = mem[i-1] + data[i]

for _ in range(M):
    a, b = map(int, input().split())
    print(mem[b-1] - mem[a-2])
