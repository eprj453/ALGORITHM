min_cmd = 0xfffff
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(visited, q):
    robot_x, robot_y, robot_dir, robot_dis = q.pop(0)
    if robot_x == x-1 and robot_y == y-1:
        return robot_dis+1 if robot_dir != z else robot_dis

    for


n, m = int(input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
x, y, z = map(int, input().split())
des_x, des_y, des_d = map(int, input().split())
visited = [[False] * m for _ in range(n)]


