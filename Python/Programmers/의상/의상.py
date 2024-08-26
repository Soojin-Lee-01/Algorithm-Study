def solution(clothes):
    dp = {}

    for cloth, kind in clothes:
        if kind in dp:
            dp[kind] += 1
        else:
            dp[kind] = 1

    total_cases = 1
    for count in dp.values():  # 생각을 해보면 (n+1)(m+1) = nm + n + m + 1
        total_cases *= (count + 1)

    return total_cases - 1
