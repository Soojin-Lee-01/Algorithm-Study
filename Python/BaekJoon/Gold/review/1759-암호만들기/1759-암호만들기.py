L, C = map(int, input().split())
data = list(map(str, input().split()))

data.sort()
set_data = []

def corret(word):
    a = 0
    b = 0
    for n in word:
        if n in ('a', 'e', 'i', 'o', 'u'):
            a += 1
        else:
            b += 1
    if a >= 1 and b >= 2:
        return True
    return False

def dfs(temp, count):
    if corret(temp) and len(temp) == L:
        print(temp)
        return

    for i in range(count, len(data)):
        dfs(temp + data[i], i+1)

dfs("", 0)
