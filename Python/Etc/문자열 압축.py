word = input()

answer = ''
temp = ''
count = 0

for i in range(len(word)):
    if i == 0:
        temp = word[i]
        count += 1
    else:
        if word[i] == temp:
            count += 1
        else:
            answer += temp
            if count > 1:
                answer += str(count)
            temp = word[i]
            count = 1

answer += temp
if count > 1:
    answer += str(count)

print(answer)


