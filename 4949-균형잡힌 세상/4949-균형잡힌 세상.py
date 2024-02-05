import sys

while True:
    word = sys.stdin.readline().rstrip()
    if word == '.':
        break
    stack = []
    result = 0
    for i in range(len(word)):
        if word[i] == "(" or word[i] == "[":
            stack.append(word[i])
        elif word[i] == ")":
            if len(stack) > 0:
                if stack[len(stack)-1] == "(":
                    stack.pop()
                else:
                    result = -1
            else:
                result = -1
        elif word[i] == "]":
            if len(stack) > 0:
                if stack[len(stack)-1] == "[":
                    stack.pop()
                else:
                    result = -1
            else:
                result = -1
    if len(stack) == 0 and result == 0:
        print("yes")
    else:
        print("no")

