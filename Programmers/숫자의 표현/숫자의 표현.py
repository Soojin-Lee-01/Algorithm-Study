# 브루트 포스 문제 - 완전 탐색 문제
def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum_n = 0
        for j in range(i, n+1):
            sum_n += j
            if sum_n == n:
                answer += 1
            elif sum_n > n:
                break
    return answer