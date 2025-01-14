"""
코드 review
1. Idea
- 거꾸로 생각해보자!
1 경우 ) 뒤에 A가 있다면, 제거
2 경우 ) 뒤에 B가 있다면, 제거 후 뒤짚
만약! 문자의 길이가 같다면 판별 후 break!

2. 시간 복잡도
최대 : O(T의 길이 ** 2)
"""
S = list(input())
T = list(input())

answer = 1

while True:
    if len(S) == len(T):
        if S == T:
            break
        else:
            answer = 0
            break
    else:
        if T[len(T)-1] == 'A':
            T.pop()
        else:
            T.pop()
            T.reverse()

print(answer)
