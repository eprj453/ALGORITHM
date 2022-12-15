from pprint import pprint
from typing import final

def solution(maps):
    answer = 0
    n, m = len(maps[0]), len(maps)
    visited = [[False] * n for _ in range(m)]
    
    maps = [list(v) for v in maps]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(m):
        for j in range(n):
            if maps[i][j] != '.' and not visited[i][j]:
                visited[i][j] = True
                land_dict = dict()
                land_dict[maps[i][j]] = [(i, j)]

                bfs = [(i, j)]

                while bfs:
                    x, y = bfs.pop(0)
                    for dx, dy in dirs:
                        if 0 <= x+dx < m and 0 <= y+dy < n and maps[x+dx][y+dy] != '.' and not visited[x+dx][y+dy]:
                            visited[x+dx][y+dy] = True
                            bfs.append((x+dx, y+dy))
                            land_dict[maps[x+dx][y+dy]] = land_dict.get(maps[x+dx][y+dy], [])
                            land_dict[maps[x+dx][y+dy]].append((x+dx, y+dy))
                
                # print(land_dict)
                max_land = max([len(v) for v in land_dict.values()])
                # print(max_land)
                max_country = []
                for k, v in land_dict.items():
                    if len(v) == max_land:
                        max_country.append(k)
                
                win_country = sorted(max_country)[-1]

                for k, v in land_dict.items():
                    if len(v) < max_land:
                        
                        for rx, ry in v:
                            # print(type(rx), ry)
                            maps[rx][ry] = win_country
    
    final_land = dict()
    
    for i in range(m):
        for j in range(n):
            if maps[i][j] != '.':
                final_land[maps[i][j]] = final_land.get(maps[i][j], 0) + 1
    
    answer = max(final_land.values())

    return answer

# print([list(v) for v in ["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]])
a = solution(["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"])
print(a)