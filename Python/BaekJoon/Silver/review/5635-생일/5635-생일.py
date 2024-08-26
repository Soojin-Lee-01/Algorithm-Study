num = int(input())

age = []

for i in range(num):
    data = list(map(str, input().split(' ')))
    age.append(data)

for i in range(num):
    age[i][1] = int(age[i][1])
    age[i][2] = int(age[i][2])
    age[i][3] = int(age[i][3])

age = sorted(age, key=lambda x: (x[3], x[2], x[1]))

print(age[len(age)-1][0])
print(age[0][0])