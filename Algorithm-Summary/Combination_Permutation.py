# 1-1. 조합 -> 중복 x
result = []
virus = [1, 2, 3, 4]
def combination(n, start = 0, combo = []):
    if len(combo) == n:
        result.append(combo[:])
        return
    for i in range(start, len(virus)):
        combo.append(virus[i])
        combination(n, i+1, combo)
        combo.pop()

combination(2)
print(result)


# 1-2. 조합 -> 중복 o
result2 = []
virus2 = [1, 2, 3, 4]
def combination2(n, start = 0, combo = []):
    if len(combo) == n:
        result2.append(combo[:])
        return
    for i in range(start, len(virus2)):
        combo.append(virus2[i])
        combination2(n, i, combo)
        combo.pop()
combination2(2)
print(result2)

# 2-1. 순열 -> 중복 x
result3 = []
virus3 = [1, 2, 3, 4]
def permutation(n, combo =[]):
    if len(combo) == n:
        result3.append(combo[:])
        return
    for element in virus3:
        if element not in combo:
            combo.append(element)
            permutation(n, combo)
            combo.pop()
permutation(2)
print(result3)

# 2-2. 순열 -> 중복 o
result4 = []
virus4 = [1, 2, 3, 4]
def permutation_with_replacement(n, combo =[]):
    if len(combo) == n:
        result4.append(combo[:])
        return
    for element in virus4:
        combo.append(element)
        permutation_with_replacement(n, combo)
        combo.pop()

permutation_with_replacement(2)
print(result4)