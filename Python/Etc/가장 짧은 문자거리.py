word, n = map(str, input().split(" "))

data = [0 for _ in range(len(word))]

temp = []

for i in range(len(word)):
    if word[i] == n:
        temp.append(i)

check = 0
for i in range(len(temp)):
    te = temp[i]

    for j in range(len(word)):
        if j < te:
            if check == 0:
                data[j] = te - j
            else:
                if data[j] > te - j:
                    data[j] = te - j
        elif j > te:
            if check == 0:
                data[j] = j - te
            else:
                if data[j] > j - te:
                    data[j] = j - te
        else:
            data[j] = 0
    check = 1

for n in data:
    print(n, end=' ')
