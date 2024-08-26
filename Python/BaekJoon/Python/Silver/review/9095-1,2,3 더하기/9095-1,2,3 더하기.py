test = int(input())
virus2 = [1,2,3]

def permutation(n, num, combo = []):
    global count
    if len(combo) == n:
        if sum(combo) == num:
            count += 1
        return
    for element in virus2:
        combo.append(element)
        permutation(n, num, combo)
        combo.pop()

for i in range(test):
    data = int(input())
    count = 0
    for j in range(1, data+1):
        permutation(j, data)
    print(count)