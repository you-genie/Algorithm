def solution(plans):
    
    def time2min(timestring: str) -> int:
        H, M = timestring.split(":")
        return int(H)*60 + int(M)

    for plan in plans:
        plan[1], plan[2] = time2min(plan[1]), int(plan[2])
        
    plans = sorted(plans, key=lambda x: x[1])
    print(plans)
    answer = []
    ready_stack = []
    
    while plans:
    # while plans or ready_stack:
        name, time, dur = plans.pop(0)
        if plans and time + dur > plans[0][1]:
            # 과제 못끝냄
            ready_stack.append((name, time+dur-plans[0][1]))
            continue
        else:
            # 과제 끝냄
            answer.append(name)
            curr_time = time + dur
            # 만약에 남은 게 있다면? 다음 과제 전까지 열심히 해 보자
            next_start_time = plans[0][1] if plans else 1440
            
            while ready_stack:
                if curr_time >= next_start_time:
                    break
                else:
                    name, durr = ready_stack.pop()
                    if curr_time + durr > next_start_time:
                        # 과제 못끝냄. 다시 들어가
                        ready_stack.append((name, curr_time + durr - next_start_time))
                        curr_time = next_start_time
                    else:
                        # 과제 끝냄.
                        answer.append(name)
                        curr_time += durr
    
    while ready_stack:
        answer.append(ready_stack.pop()[0])

    return answer