sentence = list(input().split(' '))

answer = ''

for word in sentence:
    if len(word) > len(answer):
        answer = word

print(answer)
