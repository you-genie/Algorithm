from collections import deque

def solution(ingredient):
    right_burger = [1, 2, 3, 1]
    burger_stack = []
    answer = 0
    
    for piece in ingredient:
        burger_stack.append(piece)
        if burger_stack[-4:] == right_burger:
            for _ in range(4):
                burger_stack.pop()
            answer += 1
                
    return answer