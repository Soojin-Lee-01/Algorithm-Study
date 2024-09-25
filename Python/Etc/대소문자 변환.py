sentence = input()
answer = ''
for i in range(len(sentence)):
    if sentence[i].islower():
        answer += sentence[i].upper()
    elif sentence[i].isupper():
        answer += sentence[i].lower()

print(answer)
