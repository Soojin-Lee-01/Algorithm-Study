word = list(map(str, input().rstrip()))

dic = {}

for i in range(len(word)):
    if word[i] in dic:
        dic[word[i]] += 1
    else:
        dic[word[i]] = 1

result = ''
count = 0
final = ''
for i in dic:
    if dic[i] % 2 == 0:
        result += (i * (dic[i]//2))
    elif dic[i] % 2 == 1:
        if count == 0:
            count += 1
            result += (i * (dic[i]//2))

            final = i * (dic[i] - (2 * (dic[i]//2)))
        else:
            print("I'm Sorry Hansoo")
            exit()

result = sorted(result)

print(''.join(map(str, result)) + final + ''.join(map(str, result[::-1])))