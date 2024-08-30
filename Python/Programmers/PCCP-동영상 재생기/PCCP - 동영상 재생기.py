def solution(video_len, pos, op_start, op_end, commands):

    # 모든 시간을 초 단위로 바꿔주자
    def min_switch(num):
        return (int(num[:2]) * 60) + int(num[3:])

    answer = ''

    video_len = min_switch(video_len)
    pos = min_switch(pos)
    op_start = min_switch(op_start)
    op_end = min_switch(op_end)

    for word in commands:
        if word == 'next':
            if op_start <= pos <= op_end:
                pos = op_end
                pos += 10
            else:
                pos += 10

        elif word == 'prev':
            if op_start <= pos <= op_end:
                pos = op_end
                pos -= 10
            else:
                pos -= 10

        if pos > video_len:
            pos = video_len
        if pos < 0:
            pos = 0
   
    if op_start <= pos <= op_end:
        pos = op_end

    hour = pos // 60
    m = pos % 60
   
    return f"{hour:02}:{m:02}"
