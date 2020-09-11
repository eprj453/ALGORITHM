def can_build_or_delete(build_dict, build):
    x, y, a, b = build
    if not a: # 기둥
        if b: # 설치
            if not y or build_dict.get((x-1, y, 1)) or build_dict.get((x+1, y, 1)) or build_dict.get((x, y-1, 0)): # 바닥이거나 보의 한쪽 끝이거나 밑에 기둥이 있거나
                return True
        else: #삭제
            if build_dict.get((x, y+1, 1)): # 기둥 오른쪽 방향으로 지탱하고 있는 보가 있다면
                if build_dict.get((x+1, y+1, 1)) or build_dict.get((x+1, y, 0)): # 그 보가 다른 보와 연결되어 있거나 다른 기둥 위에 있는 보라면
                    return True
            if build_dict.get((x-1, y+1, 1)): # 기둥 왼쪽 방향으로 지탱하고 있는 보가 있다면
                if build_dict.get((x-2, y+1, 1)) or build_dict.get((x-1, y, 0)):
                    return True
    else: # 보
        if b: # 설치
            if build_dict.get((x, y-1, 0)) or build_dict.get((x+1, y-1, 0)) or \
                    (build_dict.get((x-1, y, 1)) and build_dict.get((x+1, y, 1))):
                return True
        else: # 삭제
            if build_dict.get((x, y, 1)):
                if build_dict.get((x-1, y, 0)):
                    return True
            if not build_dict.get((x+1, y, 1)) and not build_dict.get((x+1, y, 0)): # 연결되어 있는 보도 없고 받치고 있는 기둥도 없을 경우
                return True

    return False

def solution(n, build_frame):
    build_dict = {}

    for build in build_frame:
        x, y, a, b = build
        if can_build_or_delete(build_dict, build):
            if b: # 설치
                build_dict[(x, y, a)] = True
            else:
                build_dict[(x, y, a)] = False
                # build_dict.get((x, y, a)):
                # build_dict.pop((x, y, a))
                    # del build_dict[(x, y, a)]
    answer = [list(x) for x in sorted(list(build_dict.keys()), key=lambda x:(x[0], x[1], x[2])) if build_dict.get(x)]
    return answer
    # return list(map(lambda x:list(x), sorted(list(build_dict.keys()), key=(x[0], x[1], x[2]))))


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))