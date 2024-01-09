from datetime import datetime, timedelta
import heapq    
    
def solution(book_time):
    ready_queue = []
    
    answer = 0
    format_book_time = []
    for start, end in book_time:
        s_h, s_m = start.split(":")
        e_h, e_m = end.split(":")
        start_time = datetime(year=2024, month=1, day=1, hour=int(s_h), minute=int(s_m))
        end_time = datetime(year=2024, month=1, day=1, hour=int(e_h), minute=int(e_m)) + timedelta(minutes=10)
        format_book_time.append((start_time, end_time))
    
    format_book_time = sorted(format_book_time, key=lambda x: (x[0], x[1]))
    # print(format_book_time)
    for i, format_time in enumerate(format_book_time):
        start, end = format_time
        heapq.heappush(ready_queue, end)
        if len(ready_queue) > answer:
            answer += 1
        while ready_queue:
            end = heapq.heappop(ready_queue)
            if i == len(format_book_time) - 1 or end > format_book_time[i+1][0]:
                heapq.heappush(ready_queue, end)
                break
    
    return answer