import sys
sys.stdin = open('5188_input.txt', 'r')

def search(tempSum, x, y):
    global ans

    if x == n-1 and y == n-1:
        ans = min(ans, tempSum)
        return

    if tempSum >= ans:
        return

    for k in range(2):
        if 0 <= x + dx[k] < n and 0 <= y + dy[k] < n:
            search(tempSum + maps[x+dx[k]][y+dy[k]], x+dx[k], y+dy[k])






for i in range(1, int(input())+1):

    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    ans = 1300
    dx, dy = [1, 0], [0, 1]
    search(maps[0][0], 0, 0)
    print("#{} {}".format(i, ans))
# def search(x, y, count, num_sum):
#     global min_sum
#     if count == (n-1) * 2:
#         min_sum = min(min_sum, num_sum)
#         return
#
#     if x + 1 < n:
#         search(x+1, y, count+1, num_sum + nums[x+1][y])
#     if y + 1 < n:
#         search(x, y+1, count+1, num_sum + nums[x][y+1])
#
#
# for i in range(1, int(input())+1):
#     n = int(input())
#     nums = [list(map(int, input().split())) for _ in range(n)]
#     dx, dy = [0, 1], [1, 0]
#     min_sum = 1690
#     search(0, 0, 0, nums[0][0])
#     print('#{} {}'.format(i, min_sum))