def solution(N, stages):
    length = len(stages)
    stage_dict = {}
    for i in range(1, N + 1):
        count = stages.count(i)
        if count == 0:
            fail = 0
        else:
            fail = count / length
        stage_dict[i] = fail
        length -= count
    stage_list = sorted([[k, v] for k, v in stage_dict.items()], key=lambda x: x[1], reverse=True)
    return [x[0] for x in stage_list]