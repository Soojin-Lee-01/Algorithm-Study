num = int(input())

dic = {}

for _ in range(num):
    data = input().split()
    if data[0] == "add":
        dic[data[1]] = data[2]
    elif data[0] == "remove":
        dic.pop(data[1])
    elif data[0] == "find":
        if data[1] in dic:
            print(dic[data[1]])
        else:
            print("None")
