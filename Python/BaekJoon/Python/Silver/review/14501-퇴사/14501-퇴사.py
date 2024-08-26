n = int(input())

data = []

for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

# dp 결과를 담을 리스트
mem = [0] * (len(data)+1)

# 거꾸로 돌면서 체크!
for i in range(len(data)-1, -1, -1):
    # 만약에 시간이 부족하면 그대로 둔다
    if data[i][0] > n-i:
        mem[i] = mem[i+1]
    # 시간이 부족하지 않다면, 더해줌
    else:
        mem[i] = max(data[i][1] + mem[i+data[i][0]], mem[i+1])
print(mem[0])
