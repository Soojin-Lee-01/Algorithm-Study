word = input()

lt = 0
rt = len(word)-1

word = word.upper()

while (lt < rt):
    if word[lt] == word[rt]:
        lt += 1
        rt -= 1
    else:
        print("NO")
        exit()

print("YES")
