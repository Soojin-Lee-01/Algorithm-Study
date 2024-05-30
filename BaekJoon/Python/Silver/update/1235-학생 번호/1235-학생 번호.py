num = int(input())

data = []
for i in range(num):
    word = list(map(int, input().rstrip()))
    data.append(word)

temp = set()
number = len(data[0])-1
while True:
    for j in range(num):
        temp.add(tuple(data[j][number:]))
    if len(temp) == num:
        print(len(data[0])-number)
        exit()
    else:
        number -= 1
        temp.clear()