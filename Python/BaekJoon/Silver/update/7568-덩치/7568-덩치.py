num = int(input())

person = []

for _ in range(num):
    data = list(map(int, input().split()))
    person.append(data)

for i in range(num):
    count = 0
    for j in range(num):
        if i != j:
            if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
                count += 1
    print(count + 1, end = " ")
