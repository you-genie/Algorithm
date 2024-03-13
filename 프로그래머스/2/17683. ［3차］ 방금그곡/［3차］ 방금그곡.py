def time2min(timestamp: str):
    HH, MM = map(int, timestamp.split(":"))
    return HH*60+MM

def encode(code: str):
    code = code.replace('B#', 'b').replace('C#', '0').replace('D#', '1').replace('F#', '2').replace('G#', '3').replace('A#', '4')
    return code
            

def solution(m, musicinfos):
    answers = []
    m = encode(m)
    for idx, musicinfo in enumerate(musicinfos):
        start, end, name, code = musicinfo.split(',')
        code = encode(code)
        delta = time2min(end) - time2min(start)
        share, remainder = delta//len(code), delta%len(code)
        total_code = code*share + code[:remainder]
        # print(total_code)
        if m in total_code:
            answers.append((delta, name, -idx))
        
    if answers:
        answer = max(answers, key=lambda x: (x[0], x[2]))
        return answer[1]
    else:
        return "(None)"