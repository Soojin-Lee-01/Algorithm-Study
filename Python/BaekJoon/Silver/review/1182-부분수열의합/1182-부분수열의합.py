N, S = map(int, input().split())
data = list(map(int, input().split()))

answer = 0

def dfs(idx, total):
    global answer
    if idx == N:
        if total == S:
            answer += 1
        return

    dfs(idx + 1, total + data[idx])
    dfs(idx + 1, total)

dfs(0, 0)

if S == 0:
    answer -= 1

print(answer)

