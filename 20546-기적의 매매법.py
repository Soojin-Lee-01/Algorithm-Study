import sys

cash = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().rstrip().split(' ')))

money_1 = cash
buy_1 = 0

money_2 = cash
buy_2 = 0

# 준현
for i in data:
    if money_1 >= i:
        buy_1 = money_1 // i
        money_1 -= (buy_1 * i)

# 성민
max = []

for i in range(1, len(data)):
    if data[i] - data[i-1] > 0:
        max.append("+")
    elif data[i] - data[i-1] < 0:
        max.append("-")
    else:
        max.append("=")

buy = 0

result = []
for i in range(len(max)):
    if max[i] == '+':
        if result.count('--') > 0:
            result.remove('--')
        result.append('++')
        if result.count('++') >= 3:
            money_2 += buy_2 * data[i+1]
            buy_2 = 0
    elif max[i] == '-':
        if result.count('++') > 0:
            result.remove('++')
        result.append('--')
        if result.count('--') >= 3:
            if money_2 >= data[i+1]:
                buy = money_2 // data[i+1]
                buy_2 += buy
                money_2 -= (buy * data[i+1])
                buy = 0
                result.remove('--')


jun = money_1 + (data[13] * buy_1)
sung = money_2 + (data[13] * buy_2)

if jun > sung:
    print('BNP')
elif jun < sung:
    print('TIMING')
else:
    print('SAMESAME')