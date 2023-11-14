import sys

N = int(sys.stdin.readline())

for j in range(N):
    stack = []
    word = list(sys.stdin.readline().rstrip())
    for i in word:
        if i == "(":
            stack.append("(")
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if len(stack) > 0:
            print("NO")
        else:
            print("YES")
