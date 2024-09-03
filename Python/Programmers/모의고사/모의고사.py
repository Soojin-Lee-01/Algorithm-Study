def solution(answers):
    pattern = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == pattern[j][i % len(pattern[j])]:
                scores[j] += 1
    
    max_score = max(scores)
    
    final = []
    for i in range(len(scores)):
        if scores[i] == max_score:
            final.append(i+1)
    final.sort()
    return final
