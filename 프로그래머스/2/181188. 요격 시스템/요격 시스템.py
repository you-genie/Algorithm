def solution(targets):
    sorted_targets = sorted(targets, key=lambda x: x[0])
    o_s, o_e = -1, -1 # 0 <= s ..............
    answer = 0
    
    for s, e in sorted_targets:
        if o_e <= s:
            # not overlap, 미사일 추가
            answer += 1
            o_s, o_e = s, e
        else:
            # overlap, 미사일 구간만 변경
            o_s = max(o_s, s)
            o_e = min(o_e, e)
    
    return answer