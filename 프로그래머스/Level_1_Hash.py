def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant.pop(-1)


participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

print(solution(participant, completion))