# Solution 1)

# 90도 회전
def rotate_90(list_2d):
    n = len(list_2d)
    m = len(list_2d[0])
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = list_2d[i][j]
    
    return new

# 180도 회전
def rotate_180(list_2d):
    n = len(list_2d)
    m = len(list_2d[0])
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[m-j-1][n-i-1] = list_2d[i][j]
    
    return new

# 270도 회전
def rotate_270(list_2d):
    n = len(list_2d)
    m = len(list_2d[0])
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[m-j-1][i] = list_2d[i][j]
    
    return new
# 90도 반시계 회전
def rotate_90_counter(list_2d):
    n = len(list_2d)
    m = len(list_2d[0])
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[m-j-1][i] = list_2d[i][j]
    
    return new

# Solution 2)

# 90도 회전
def rotated_90(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(e) for e in list_of_tuples]

# 90도 반시계 회전
def rotate_90_counter(list_2d):
    return [list(row)[::-1] for row in zip(*list_2d)]
