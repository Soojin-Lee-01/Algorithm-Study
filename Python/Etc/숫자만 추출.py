word = input()

new = ''

for i in range(len(word)):
    if word[i].isalpha():
        pass
    else:
        new += word[i]

print(int(new))
