n = int(input())
result = []
for i in range(n):
    num = int(input())
    if num != 0:
        result.append(num)
    elif num == 0:
        if len(result) > 0:
            result.pop()
        else:
            pass

print(sum(result))