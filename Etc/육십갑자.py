T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    one_list = list(map(str, input().split()))
    two_list = list(map(str, input().split()))

    result = []
    test = int(input())
    for j in range(test):
        num = int(input())
        temp = ''
        temp += one_list[(num % N) - 1]
        temp += two_list[(num % M) - 1]
        result.append(temp)

    print("#" + str(i + 1), ' '.join(map(str, result)))