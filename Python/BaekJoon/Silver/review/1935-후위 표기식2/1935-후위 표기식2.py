import sys

N = int(sys.stdin.readline())

word = sys.stdin.readline().rstrip()

operator = ["+", "-", "*", "/"]

dic = {}
for i in range(N):
    number = float(sys.stdin.readline())
    dic[chr(65 + i)] = number

stack = []

for i in range(len(word)):
    if word[i] not in operator:
        stack.append(dic[word[i]])
    else:
        a = stack.pop()
        b = stack.pop()
        if word[i] == "+":
            stack.append(b + a)
        elif word[i] == "-":
            stack.append(b - a)
        elif word[i] == "*":
            stack.append(b * a)
        else:
            stack.append(b / a)

print(format(stack[0], '.2f'))




