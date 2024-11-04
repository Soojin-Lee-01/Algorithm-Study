def answer(cals, scores, L):
    num = len(cals)

    dp = [[0 for _ in range(L+1)] for _ in range(num+1)]

    for i in range(1, num+1):
        for w in range(1, L+1):
            if cals[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cals[i-1]] + scores[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[num][L]

n = int(input())

for i in range(n):
    N, L = map(int, input().split())
    scores = []
    cals = []
    for j in range(N):
        score, cal = map(int, input().split())
        scores.append(score)
        cals.append(cal)
    print(f'#{i+1} {answer(cals, scores, L)}')
