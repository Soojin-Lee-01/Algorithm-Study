def solution(s):
    answer = 0    
    temp  = 1
    result = 1e9
    for i in range(1, len(s)+1):
        data = []
        for j in range(0, len(s), i):
            data.append(s[j:j+temp])
        
        te = ""
        co = 0
        tt = 0
        for j in range(len(data)):      
            if j == 0:
                te = data[j]
                co += 1
            else:
                if (data[j] == te):
                    co+= 1                 
                else:               
                    if co == 1:
                        tt += len(str(te))
                    else:
                        tt += (len(str(co)) + len(te))                
                    te = data[j]
                    co = 1
        if co == 1:
            tt += len(str(te))
        else:
            tt += (len(str(co)) + len(te))
        result = min(tt, result)
         
        temp+=1
    
    return result
