def solution(A, B):
    answer = 0

    a = sorted(A, reverse=True)
    b = sorted(B)
    for i in range(len(a)):
        answer += (a[i] * b[i])

    return answer