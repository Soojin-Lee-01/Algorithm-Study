import sys

n = int(sys.stdin.readline())

def num(list):
    result = []
    if ' ' in list:
        list.remove(' ')
    count = {}
    for i in list:
        try: count[i] += 1
        except: count[i] = 1
    count.pop(' ', None)
    max_num = max(count.values())
    for j in count.values():
        if j == max_num:
            a = {v:k for k, v in count.items()}
            result.append(a.get(j))
    if len(result) > 1:
        return "?"
    else:
        return result[0]

for i in range(n):
    word = list(str(sys.stdin.readline().rstrip()))
    print(num(word))