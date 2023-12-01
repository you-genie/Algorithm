import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    num_works = 0
    max_days = deque([])
    for progress, speed in zip(progresses, speeds):
        max_days.append(math.ceil((100 - progress) / speed))
    
    m_d = max_days.popleft()
    cnt = 1
    while max_days:
        if (d := max_days.popleft()) > m_d:
            answer.append(cnt)
            m_d = d
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)    
    return answer