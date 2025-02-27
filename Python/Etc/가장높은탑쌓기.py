N = int(input())
blocks = []
for _ in range(N):
    data = list(map(int, input().split()))
    blocks.append(data)

blocks = sorted(blocks, key=lambda x : (-x[0]))

mem = [0] * (N+1)

mem[0] = blocks[0][1]

for i in range(1, N):
    mem[i] = blocks[i][1]
    for j in range(i):
        if blocks[i][2] < blocks[j][2]:
            mem[i] = max(mem[i], mem[j] + blocks[i][1])

print(max(mem))
