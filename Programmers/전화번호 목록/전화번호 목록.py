def solution(book):
    dic = {}
    for i in book:
        dic[i] = 1
    for nums in book:
        temp = ''
        for num in nums:
            temp += num

            if temp in dic and temp != nums:
                return False
    return True