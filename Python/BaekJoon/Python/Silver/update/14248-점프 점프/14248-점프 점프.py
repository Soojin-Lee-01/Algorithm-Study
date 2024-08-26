"""
dfs 문제! 차근차근 생각해보자.
먼저 방문을 담는 것을 만들고
시작 기준 오른쪽, 왼쪽을 비교해서 카운트해주고 방문처리를 해준다.
"""

N = int(input())

data = list(map(int, input().split()))

start = int(input())

cnt = 1

visited = [0] * N

def dfs(x):
    global cnt
    for nx in (x + data[x], x- data[x]):
        if 0 <= nx < N and visited[nx] == 0:
            cnt += 1
            visited[nx] = 1
            dfs(nx)

dfs(start-1)
print(cnt)
