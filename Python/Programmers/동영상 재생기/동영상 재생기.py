def solution(video_len, pos, op_start, op_end, commands):
    def time_change(str):
        return int(str[:2]) * 60 + int(str[3:])
    # 현재 시간
    current_time = time_change(pos)
    
    # 오프닝 시간 시작 & 끝
    start_time = time_change(op_start)
    end_time = time_change(op_end)
    
    # 비디오 길이
    video = time_change(video_len)
    
    temp_answer = 0
    
    if start_time <= current_time <= end_time:
        current_time = end_time
    
    for num in commands:
        if num == "next":
            current_time += 10
            if current_time >= video:
                current_time = video
            if start_time <= current_time <= end_time:
                current_time = end_time
        elif num == "prev":
            current_time -= 10
            if current_time < 0:
                current_time = 0
            if start_time <= current_time <= end_time:
                current_time = end_time
                
    hour = str(current_time // 60).zfill(2)
    minute = str(current_time % 60).zfill(2)
    
    return hour + ':' + minute
