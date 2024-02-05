import sys
from collections import deque

index = []

word = sys.stdin.readline().rstrip()

for i in range(len(word)):
    if word[i] == "<" or word[i] == ">":
        index.append(i)

temp = deque()
for i in range(0, len(index), 2):
    temp.append(word[index[i]:index[i+1]+1])

for i in temp:
    word = word.replace(i, ' ~ ')

word = word.split(' ')

result = []
for i in range(len(word)):
    if word[i] == '':
        pass
    elif word[i] == '~':

        result.append(temp[0])
        temp.popleft()
    else:
        result.append(word[i][::-1])

last = ' '.join(map(str, result))

last = last.replace('> ', '>')
last = last.replace(' <', '<')
print(last)



