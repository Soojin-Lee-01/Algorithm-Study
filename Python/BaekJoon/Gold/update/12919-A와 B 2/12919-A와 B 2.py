"""
메모리가 초과할 수 있으므로, 길이가 긴 문자열을 길이가 작은 문자열로 바꾸는 식으로 확인!

1) 만약에 문자열 뒤에 A가 있다면 제거
2) 만약에 문자열 앞에 B가 있다면 제거하고 뒤집기
"""

S = input()
T = input()
answer = 0

def dfs(str):
    global answer
    if str == S:
        answer = 1
        return
    if len(str) == 0:
        return

    if str[-1] == 'A':
        dfs(str[:-1])
    if str[0] == 'B':
        dfs(str[1:][::-1])

dfs(T)
print(answer)
