def solution(record):
    answer = []
    dict1 = {}

    for r in record:
        r_split = r.split(' ')
        if r_split[0] == 'Enter' or r_split[0] == 'Change':
            dict1[r_split[1]] = r_split[2]

    for r in record:
        r_split = r.split(' ')
        if r_split[0] == 'Enter':
            answer.append(dict1[r_split[1]] + '님이 들어왔습니다.')
        if r_split[0] == 'Leave':
            answer.append(dict1[r_split[1]] + '님이 나갔습니다.')

    print(answer)
    return answer


records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

print(solution(records))