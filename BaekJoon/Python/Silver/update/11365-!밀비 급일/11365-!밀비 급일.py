import sys

# Solution - 1
while 1:
    data = sys.stdin.readline().rstrip()
    if data == "END":
        break
    print(data[::-1])


# Solution - 2
word = []

while 1:
    data = list(map(str, sys.stdin.readline().rstrip().split(' ')))
    word.append(data)
    if data[0] == "END":
        break

for i in range(len(word)-1):
    word[i].reverse()
    for j in range(len(word[i])):
        print(''.join(word[i][j][::-1]), end=' ')
    print()
