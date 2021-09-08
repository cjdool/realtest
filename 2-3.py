import re

def solution(program, flag_rules, commands):
    answer = []
    alphalist = re.compile('[a-zA-Z]') # alphabet regular expression
    numlist = re.compile('[0-9]') # number regular expression

    # divide alias rule and normal rule
    aliaslist = []
    for rule in flag_rules:
        if 'ALIAS' in rule:
            aliaslist.append([rule.split()[0], rule.split()[2]])
            flag_rules.remove(rule)

    for command in commands:
        cmdlist = command.split() # string to list

        # first check program name
        if program != cmdlist[0]:
            answer.append(False)
            continue # goto next command

        # preprocess for alias -> change before check
        for i in range(len(cmdlist)):
           for alias in aliaslist:
                if cmdlist[i] in alias[0]:
                    cmdlist[i] = alias[1]

        i = 1 # cmdlist[0] is program name and it is already checked
        flag_name = ''
        flag_parameter = ''
        flag = True # flag for true case
        usedset = set() # set for used flag
        while i < len(cmdlist):
            if '-' in cmdlist[i]: # check it is flag_name or flag_parameter

                # flag duplication check
                if cmdlist[i] in usedset: # flag duplication
                    answer.append(False)
                    flag = False
                    break # wrong answer exist -> no more action needed
                else: # not flag duplication
                    usedset.add(cmdlist[i])

                flag_name = cmdlist[i]

                # find command argument type
                for rule in flag_rules:
                    if flag_name in rule:
                        paraname = rule.split()[1]
                        break

                if i == len(cmdlist) - 1: # last case exception
                    flag_parameter = '-' # only valid for null
                else: # not last case
                    flag_parameter = cmdlist[i+1]

                if paraname == 'STRING':
                    if alphalist.match(flag_parameter) is None: # not string case
                        answer.append(False)
                        flag = False
                        break # wrong answer exist -> no more action needed
                    else:
                        i += 1
                elif paraname == 'STRINGS':
                    # first find flag_parameters
                    j = i+1
                    paranumber = 0
                    flag_parameterlist = []
                    while j < len(cmdlist):
                        if '-' in cmdlist[j]: # find next flag_argument
                            break
                        flag_parameterlist.append(cmdlist[j])
                        j += 1

                    # check for each flag_parameter
                    flag2 = False
                    for item in flag_parameterlist:
                        if alphalist.match(item) is None: # not string case
                            answer.append(False)
                            flag = False
                            flag2 = True
                            break

                    if flag2: # wrong answer exist -> no more action needed
                        break
                    else:
                        i += len(flag_parameterlist)
                elif paraname == 'NUMBER':
                    if numlist.match(flag_parameter) is None: # not number case
                        answer.append(False)
                        flag = False
                        break # wrong answer exist -> no more action needed
                    else:
                        i += 1 # go to next flag_name
                elif paraname == 'NUMBERS':
                    # first find flag_parameters
                    j = i+1
                    paranumber = 0
                    flag_parameterlist = []
                    while j < len(cmdlist):
                        if '-' in cmdlist[j]: # find next flag_argument
                            break
                        flag_parameterlist.append(cmdlist[j])
                        j += 1

                    # check for each flag_parameter
                    flag2 = False
                    for item in flag_parameterlist:
                        if numlist.match(item) is None: # not number case
                            answer.append(False)
                            flag = False
                            flag2 = True
                            break

                    if flag2: # wrong answer exist -> no more action needed
                        break
                    else:
                        i += len(flag_parameterlist)
                else: # paraname == 'NULL'
                    if '-' not in flag_parameter: # not null case (some flag_parameter exist)
                        answer.append(False)
                        flag = False
                        i += 1
                        break # wrong answer exist -> no more action needed
            else: # no flag_argument case
                answer.append(False)
                flag = False
                break # wrong answer exist -> no more action needed
            i += 1

        if flag:
            answer.append(True)

    return answer


print(solution("line", ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"], ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]))
print(solution("bank", ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"], ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]))
print(solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -n 100 -s hi -e", "lien -s Bye"]))
print(solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"]))
print(solution("line", ["-s STRINGS", "-n NUMBERS", "-e NULL"], ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]))
print(solution("trip", ["-days NUMBERS", "-dest STRING"], ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]))