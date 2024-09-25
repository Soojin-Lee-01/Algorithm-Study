sentence = input()
answer = []
for i in range(len(sentence)):
    if sentence[i] not in answer:
        answer.append(sentence[i])

print(''.join(answer))
