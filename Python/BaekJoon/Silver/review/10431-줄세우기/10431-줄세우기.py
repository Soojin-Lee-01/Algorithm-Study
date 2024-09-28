# Solution - 1

n = int(input())

for i in range(n):
    data = list(map(int, input().split(" ")))
    data = data[1:]

    person = []
    count = 0
    for j in range(20):
        if j == 0:
            person.append(data[j])
        else:
            person.append(data[j])
            person.sort()
            for k in range(len(person)):
                if person[k] == data[j]:
                    count += len(person) - (k+1)

    print(i+1, count)

# Solution - 2 : 버블정렬

test = int(input())

for i in range(test):
    data = list(map(int, input().split(" ")))
    count = 0
    for j in range(1, len(data)-1):
        for k in range(j+1, len(data)):
            if data[j] > data[k]:
                data[j], data[k] = data[k], data[j]
                count += 1

    print(i+1, count)

