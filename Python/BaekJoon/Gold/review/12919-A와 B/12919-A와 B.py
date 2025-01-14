"""
코드 review

1. Idea
- DFS를 이용해 해결
1) 뒤에 A를 제거하거나, 앞에 B가 있으면 뒤집고 B를 제거하거나
2) 만약 형태가 같을 경우 계산이 중복되므로 visited 처리
3) 길이가 S보다 작아지는 경우 return
4) 길이가 같은데 똑같은 경우 return

"""
S = list(input())
T = list(input())

answer = 0
found = False
temp = set()
def dfs(S, T):
    global found
    global answer

    sentence = ''.join(map(str, T))
    if sentence in temp:
        return
    temp.add(sentence)

    if found:
        return
    if len(S) == len(T):
        if S == T:
            found = True
            answer = 1
        return
    elif len(S) > len(T):
        return
    else:
        if T[-1] == 'A':
            T.pop()
            dfs(S, T)
            T.append('A')
        if T[0] == 'B':
            T.reverse()
            T.pop()
            dfs(S, T)
            T.append('B')
            T.reverse()

dfs(S, T)
print(answer)
