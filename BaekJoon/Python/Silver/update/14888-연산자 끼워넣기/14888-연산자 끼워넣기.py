num = int(input())
data = list(map(int, input().split()))
operate = list(map(int, input().split()))

min_num = 1e9
max_num = -1e9

# dfs 를 이용하여 연산
def dfs(n, temp):
    global min_num, max_num

    # 만약에 n 만큼 연산을 하면, 비교 후 결과 반환
    if n == num-1:
        max_num = max(temp, max_num)
        min_num = min(temp, min_num)
        return

    # 만약에 각 연산자가 있다면 계산
    if operate[0] > 0:
        operate[0] -= 1
        dfs(n+1, temp+data[n+1])
        operate[0] += 1
    if operate[1] > 0:
        operate[1] -= 1
        dfs(n+1, temp-data[n+1])
        operate[1] += 1
    if operate[2] > 0:
        operate[2] -= 1
        dfs(n+1, temp * data[n+1])
        operate[2] += 1
    if operate[3] > 0:
        operate[3] -= 1
        dfs(n+1, int(temp/data[n+1]))
        operate[3] += 1

# 처음부터 계산 시작
dfs(0, data[0])
print(max_num)
print(min_num)
