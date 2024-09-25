sentence = input()
word = input()
answer = 0
sentence = sentence.upper()
word = word.upper()

for i in range(len(sentence)):
    if sentence[i] == word:
        answer += 1

print(answer)
