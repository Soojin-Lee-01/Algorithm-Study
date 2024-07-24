def solution(s):
    
    dic = {}
    dic["zero"] = 0
    dic["one"] = 1
    dic["two"] = 2
    dic["three"] = 3
    dic["four"] = 4
    dic["five"] = 5
    dic["six"] = 6
    dic["seven"] = 7
    dic["eight"] = 8
    dic["nine"] = 9
    
    for i in dic:
        s = s.replace(i, str(dic[i]))
        
    return int(s)
