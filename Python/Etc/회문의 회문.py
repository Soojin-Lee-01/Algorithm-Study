def solution(S):
    num = len(S)
    if S == S[::-1]:
        if S[:num//2] == S[:num//2][::-1] and S[num//2+1:] == S[num//2+1:][::-1]:
            return 'YES'
    else:
        return 'NO'
    return 'NO'

t = int(input())
for testcase in range(1, t+1):
    S = input()
    answer = solution(S)
    print("#" + str(testcase), answer)
