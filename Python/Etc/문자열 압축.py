word = input()
count = 0
answer = ""
word += ' '
for i in range(len(word)-1):
    if word[i] == word[i+1]: count += 1
    else:
        answer += word[i]
        if count > 1:
            answer += str(count)
        count = 1

print(answer)
