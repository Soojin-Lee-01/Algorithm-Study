import sys

word = sys.stdin.readline().rstrip() + ' '

stack = []
switch = 0
result = ''
for i in range(len(word)):
    if word[i] == "<":
        switch = 1
        for _ in range(len(stack)):
            result += stack.pop()
        result += '<'
    elif word[i] == ">":
        switch = 0
        for _ in range(len(stack)):
            result += stack.pop(0)
        result += '>'
    elif word[i] == ' ' and switch == 0:
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '
    else:
        stack.append(word[i])

print(result)