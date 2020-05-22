# min_cmd = 0xfffff
# dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# def bfs(visited, q):
#     robot_x, robot_y, robot_dir, robot_dis = q.pop(0)
#     if robot_x == x-1 and robot_y == y-1:
#         return robot_dis+1 if robot_dir != z else robot_dis
#
#     for
#
#
# n, m = int(input().split())
# maps = [list(map(int, input().split())) for _ in range(n)]
# x, y, z = map(int, input().split())
# des_x, des_y, des_d = map(int, input().split())
# visited = [[False] * m for _ in range(n)]
#
#

def solution(left, right):
    answer = 0
    while left and right:
        print(left, right)
        if left[0] > right[0]:
            if max(left) > right[0]:
                answer += right.pop(0)
            else:
                left.pop(0)
        else:
            if max(left) > max(right):
                left.pop(0)
            else:
                left.pop(0)
                right.pop(0)
    return answer
print(solution([10,10,10,12,10,10], [11,10,10,11,10,10]))