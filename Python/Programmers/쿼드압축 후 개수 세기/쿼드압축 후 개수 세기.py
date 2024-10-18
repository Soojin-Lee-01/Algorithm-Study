def count(gra):
    ones = 0
    zeros = 0
    for row in gra:
        ones += row.count(1)  
        zeros += row.count(0) 
    if ones == len(gra) * len(gra[0]): 
        return 1, 0
    elif zeros == len(gra) * len(gra[0]):  
        return 0, 1
    else: 
        return -1, -1  

def number(gra, a, b, c, d):
    global answer
    temp = [row[b:d] for row in gra[a:c]] 
    a_, b_ = count(temp) 
    
    if a_ == 1: 
        answer[1] += 1
        return
    elif b_ == 1: 
        answer[0] += 1
        return
    

    mid_x = (a + c) // 2
    mid_y = (b + d) // 2

    number(gra, a, b, mid_x, mid_y)  
    number(gra, a, mid_y, mid_x, d)  
    number(gra, mid_x, b, c, mid_y)  
    number(gra, mid_x, mid_y, c, d)  

answer = [0, 0] 

def solution(arr):
    global answer
    answer = [0, 0]  
    number(arr, 0, 0, len(arr), len(arr))  
    return answer
