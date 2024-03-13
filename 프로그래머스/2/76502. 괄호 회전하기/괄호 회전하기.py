from collections import deque
from typing import Deque

match_dict = {'[': ']', '{': '}', '(': ')'}

def is_valid(s: Deque) -> bool:
    s = s.copy()
    stack = deque()
    while s:
        p = s.popleft()
        if stack:
            c = stack.pop()
            if not (c in match_dict and match_dict[c] == p):
                stack.append(c)
                stack.append(p)
        else:
            stack.append(p)

    return not bool(stack)
                

def rotate_right(s: Deque) -> Deque:
    s.append(s.popleft())
    return s

def solution(s):
    s = deque(list(s))
    answer = 0
    for _ in range(len(s)):
        if is_valid(s):
            answer += 1
        s = rotate_right(s)

        
    return answer