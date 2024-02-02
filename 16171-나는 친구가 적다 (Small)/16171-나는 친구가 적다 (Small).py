import sys

word = sys.stdin.readline().rstrip()
find = sys.stdin.readline().rstrip()

new = []

for i in range(len(word)):
    if word[i].isdigit() is False:
        new.append(word[i])

new_word = ''.join(map(str, new))

if find in new_word:
    print(1)
else:
    print(0)
