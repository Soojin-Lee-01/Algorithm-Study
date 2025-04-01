def solution(rsp):
    answer = ''
    dict = {}
    dict["2"] = "0"
    dict["0"] = "5"
    dict["5"] = "2"
    
    for i in range(len(rsp)):
        answer += dict[rsp[i]]
        
    return answer
