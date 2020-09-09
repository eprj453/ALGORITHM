def solution(n, build_frame):
    bo_dict = {}
    column_dict = {}

    for build in build_frame:
        x, y, a, b = build
        if not a: # 기둥
            if not y: # 맨 밑바닥
                column_dict[(x, y)] = [1, 0] # 바닥 디디고 있음, 천장에 뭐 더 없음
            elif column_dict.get((x, y+1)) and not column_dict.get((x, y+1))[1]: # 기둥 이미 세워져있고 위에 쌓여있는 기둥 없는 경우


