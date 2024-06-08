def solution(N):
    count = 0
    while True:
        if N == 1:
            count += 1
            break
        if N % 2 == 0:
            N = N // 2
        elif N % 2 == 1:
            count += 1
            N -= 1

    return count