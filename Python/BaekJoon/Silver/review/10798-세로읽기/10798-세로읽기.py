import sys

word = []

for i in range(5):
    data = list(map(str, sys.stdin.readline().rstrip()))
    word.append(data)
max = 0
for i in range(len(word)):
    if len(word[i]) > max:
        max = len(word[i])

for i in range(len(word)):
    if len(word[i]) < max:
        for j in range(max - len(word[i])):
            word[i].append(' ')

for i in range(max):
    for j in range(5):
        if word[j][i] != ' ':
            print(word[j][i], end='')

