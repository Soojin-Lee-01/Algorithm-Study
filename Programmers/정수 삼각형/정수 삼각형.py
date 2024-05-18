def solution(triangle):
    while True:
        temp = []
        if len(triangle) == 1 and len(triangle[0]) == 1:
            return triangle[0][0]
        else:
            data = triangle.pop()
            for i in range(len(data) - 1):
                temp.append(max(data[i], data[i + 1]))
            triangle.append(temp)
            word1 = triangle.pop()
            word2 = triangle.pop()
            te = [i + j for i, j in zip(word1, word2)]
            triangle.append(te)


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))