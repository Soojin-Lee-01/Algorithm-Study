from collections import deque

def solution(s):
    answer = 0
    num= len(s)
    s = deque(s)
    for i in range(num):
        s.rotate(-1)
        stack = []
        for j in range(len(s)):
            if len(stack) == 0:
                stack.append(s[j])
            elif s[j] == '}':
                if len(stack) > 0:
                    if stack[len(stack)-1] == "{":
                        stack.pop()
                else:
                    break
            elif s[j] == ')':
                if len(stack) > 0:
                    if stack[len(stack)-1] == '(':
                        stack.pop()
                else:
                    break
            elif s[j] == ']':
                if len(stack) > 0:
                    if stack[len(stack)-1] == '[':
                        stack.pop()
                else:
                    break
            else:
                stack.append(s[j])

        if len(stack) == 0:
            answer += 1


    return answer
