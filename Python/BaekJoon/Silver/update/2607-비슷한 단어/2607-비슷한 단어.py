n = int(input())

word = list(input())

count = 0

for i in range(n-1):
    compare = word[:]
    temp = input()
    c = 0

    for w in temp:
        if w in compare:
            compare.remove(w)
        else:
            c += 1

    if c < 2 and len(compare) < 2:
        count += 1

print(count)
