word = input()

new = ''

for i in range(len(word)):
    if word[i].isalpha():
        new += word[i]

new = new.lower()

if (new == new[::-1]):
    print("YES")
else:
    print("NO")
