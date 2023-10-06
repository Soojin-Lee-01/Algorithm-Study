n, m = map(int, input().split())
result = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        result[b - 1] = c
    elif a == 2:
        for i in range(b - 1, c):
            result[i] = 1 - result[i]
    elif a == 3:
        for i in range(b - 1, c):
            result[i] = 0
    else:
        for i in range(b - 1, c):
            result[i] = 1

# 리스트를 문자열로 변환하고 공백을 기준으로 한 줄로 출력
print(" ".join(map(str, result)))