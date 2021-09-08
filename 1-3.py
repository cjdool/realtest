def solution(enter, leave):
    answer = []
    num = len(enter)
    list = [[False] * num for _ in range(num)]
    for i in range(num):
        early = enter[i+1:num-1]
        index = leave.index(enter[i])
        late = leave[0:index]
        if len(early) == 0 or len(late) == 0:
            continue
        early = enter[0:i+1]
        late = leave[index:]


    return answer