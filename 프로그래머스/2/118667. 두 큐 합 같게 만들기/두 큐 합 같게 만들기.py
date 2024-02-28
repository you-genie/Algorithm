from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    
    if sum(queue1 + queue2) % 2 == 1:
        return -1

    bucket = sum(queue1 + queue2) // 2
    
    answer = 0
    s = sum(q1)
    for _ in range(2*len(queue1) + len(queue2)):
        if s > bucket:
            q2.append(v := q1.popleft())
            answer += 1
            s -= v
        elif s < bucket:
            q1.append(v := q2.popleft())
            answer += 1
            s += v
        else:
            return answer
        
    return -1