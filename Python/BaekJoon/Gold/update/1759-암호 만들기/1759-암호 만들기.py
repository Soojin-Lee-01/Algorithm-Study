L, C = map(int, input().split())

check = ['a', 'e', 'i', 'o', 'u']

data = list(map(str, input().split()))

data.sort()

count = 0
def dfs(num, combo = []):
    global count
    if len(combo) == L:
        count = 0
        count1 = 0
        for j in combo:
            if j in check:
                count += 1
            else:
                count1 +=1
        if count >= 1 and count1 >= 2:
            print(''.join(combo))
            return

    for i in range(num, len(data)):
        combo.append(data[i])
        dfs(i+1, combo)
        combo.pop()

dfs(0)
