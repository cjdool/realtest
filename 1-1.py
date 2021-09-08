a = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
b = ["JAVA", "JAVASCRIPT"]
c = [7, 5]

def solution(table, languages, preference):
    answer = ''
    maxsum = 0
    for item in table:
        itemlist = item.split()
        sum = 0
        for i in range(len(languages)):
            if languages[i] in itemlist:
                index = itemlist.index(languages[i])
                sum += preference[i] * (6-index)
        if sum > maxsum:
            maxsum = sum
            answer = itemlist[0]
        elif sum == maxsum:
            temp = [answer]
            temp.append(itemlist[0])
            sorttemp = sorted(temp)
            answer = sorttemp[0]
    return answer

print(solution(a, b, c))