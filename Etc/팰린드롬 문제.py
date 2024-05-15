num = int(input())

for i in range(num):
    n, m = map(int, input().split(' '))
    result1 = 0
    result2 = 0
    temp = []
    for j in range(n):
        data = input()
        temp.append(data)
    for word in temp:
        if word[::-1] in temp and word != word[::-1]:
            result1 += m
        elif word[::-1] in temp:
            result2 = m
    print("#" + str(i+1), result1 + result2)
