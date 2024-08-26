import sys

money = int(sys.stdin.readline())

duck = list(map(int, sys.stdin.readline().rstrip().split(' ')))

def Jun(money):
    num = 0
    bill = money
    for i in duck:
        if i <= bill:
            num = bill // i
            bill -= (num * i)
    return (bill + duck[13] * num)

jun = Jun(money)

def Sun(money):
    num = 0
    bill = money
    data = []
    plus = 0
    minus = 0
    for i in range(1, len(duck)):
        if duck[i] < duck[i-1]:
            data.append('-')
            if len(data) > 1 and data[len(data)-2] == '-':
                minus += 1
                if minus >= 2 and duck[i] <= bill:
                    a = bill // duck[i]
                    num += a
                    bill -= a * duck[i]
                    minus = 1
                    plus = 0

        elif duck[i] > duck[i-1]:
            data.append('+')
            if len(data) > 1 and data[len(data)-2] == '+':
                plus += 1
                if plus >= 2 and num != 0:
                    bill += duck[i] * num
                    num = 0
                    plus = 1
                    minus = 0
        else:
            data.append("=")
    return (bill + duck[13] * num)

sun = Sun(money)

if jun > sun:
    print("BNP")
elif jun < sun:
    print("TIMING")
else:
    print("SAMESAME")

