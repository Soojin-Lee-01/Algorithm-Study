from collections import Counter

test = int(input())

for i in range(test):
    data = input()
    data = data.replace(' ', '')
    temp = Counter(data)
    max_num = temp.most_common()

    if len(max_num) < 2 or max_num[0][1] != max_num[1][1]:  # max_num의 길이가 2보다 작은 경우도 처리
        print(max_num[0][0])
    else:
        print("?")