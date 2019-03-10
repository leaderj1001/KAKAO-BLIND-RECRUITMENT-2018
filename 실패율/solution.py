def solution(N, stages):
    answer = []

    total_len = len(stages)

    result = []
    for number in range(1, N + 1):
        if total_len != 0:
            result.append([number, stages.count(number) / total_len])
            total_len -= stages.count(number)
        else:
            result.append([number, 0])

    result = sorted(result, key=lambda x: x[1], reverse=True)

    for r in result:
        answer.append(r[0])

    print(answer)
    return answer