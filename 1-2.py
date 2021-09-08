def solution(inp_str):
    answer = []
    lower = list('abcdefghijklmnopqrstuvwxyz')
    upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    num = list('0123456789')
    speci = list('~!@#$%^&*')
    extra = list('()-_=+')
    lowercnt = [0] * len(lower)
    uppercnt = [0] * len(upper)
    numcnt = [0] * len(num)
    specicnt = [0] * len(speci)
    extracnt = [0] * len(extra)

    # first check
    if len(inp_str) < 8 or len(inp_str) > 15:
        answer.append(1)

    # second, fourth check
    prev = ''
    cont = 0
    flag1 = True
    flag2 = True
    for let in inp_str:
        if prev == let:
            cont += 1
        if let in lower:
            index = lower.index(let)
            lowercnt[index] += 1
        elif let in upper:
            index = upper.index(let)
            uppercnt[index] += 1
        elif let in num:
            index = num.index(let)
            numcnt[index] += 1
        elif let in speci:
            index = speci.index(let)
            specicnt[index] += 1
        else:
            if flag1:
                answer.append(2)
                flag1 = False
            index = extra.index(let)
            extracnt[index] += 1
        prev = let
        if cont >= 3 and flag2:
            answer.append(4)
            flag2 = False

    cnt = [lowercnt, uppercnt, numcnt, specicnt]

    # third, fifth check
    crit = 0
    for lst in cnt:
        if sum(lst) > 0:
            crit += 1
        flag = False
        if not flag:
            for item in lst:
                if item >= 5:
                    answer.append(5)
                    flag = True
                    break

    if crit < 3:
        answer.append(3)

    if 5 not in answer:
        for item in extracnt:
            if item >= 5:
                answer.append(5)
                break

    answer.sort()

    if len(answer) == 0:
        answer.append(0)

    return answer

print(solution("AaTa+!12-3"))
print(solution("aaaaZZZZ)"))
print(solution("CaCbCgCdC888834A"))
print(solution("UUUUU"))
print(solution("ZzZz9Z824"))