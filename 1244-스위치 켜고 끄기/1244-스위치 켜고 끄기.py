import sys

n = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().rstrip().split(' ')))
student = int(sys.stdin.readline())

for i in range(student):
    sex, number = map(int, sys.stdin.readline().split(' '))
    if sex == 1:
        for j in range(n):
            if (j + 1) % number == 0:
                if switch[j] == 0:
                    switch[j] = 1
                else:
                    switch[j] = 0
    else:
        stop = [number-1]
        for m in range(1, number):
            if number-m-1 >= 0 and number-1+m <= (n-1):
                if switch[number-m-1] == switch[number-1+m]:
                    stop.append(number-m-1)
                    stop.append(number-1+m)
                else:
                    break
        for v in stop:
            if switch[v] == 1:
                switch[v] = 0
            else:
                switch[v] = 1


for i in range(1, n+1):
    print(switch[i-1], end= " ")
    if i % 20 == 0:
        print()