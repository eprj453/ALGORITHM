import sys
sys.stdin = open('1873_input.txt', 'r')
for i in range(1, int(input())+1):
    h, w = map(int, input().split())
    field = [list(input()) for _ in range(h)]
    # print(field)
    n = int(input())
    command = list(input())
    d_x, d_y, my_x, my_y = 0, 0, 0, 0
    dx, dy, dir, d_command = [0, -1, 1, 0], [-1, 0, 0, 1], ['<', '^', 'v', '>'], 'LUDR'
    my_dir = ''

    for j in range(h):
        if my_dir: break
        for k in range(w):
            if field[j][k] == '<' or field[j][k] == 'v' or field[j][k] == '>' or field[j][k] == '^':
                my_dir, my_x, my_y = field[j][k], j, k
                d_x, d_y = dx[dir.index(my_dir)], dy[dir.index(my_dir)]
                break
    for c in command:
        if c == 'S':
            cannon_x, cannon_y = my_x + d_x, my_y + d_y
            while 0 <= cannon_x < h and 0 <= cannon_y < w:
                if field[cannon_x][cannon_y] == '#':
                    break
                elif field[cannon_x][cannon_y] == '*':
                    field[cannon_x][cannon_y] = '.'
                    break
                cannon_x += d_x
                cannon_y += d_y

        else:
            idx = d_command.index(c)
            d_x, d_y = dx[idx], dy[idx]
            field[my_x][my_y] = dir[idx]
            if 0 <= my_x + d_x < h and 0 <= my_y + d_y < w and field[my_x+d_x][my_y+d_y] == '.':
                field[my_x][my_y] = '.'
                field[my_x + d_x][my_y + d_y] = dir[idx]
                my_x += d_x
                my_y += d_y

    print('#{}'.format(i), end = ' ')
    for j in range(h):
        print(''.join(field[j]))





'''
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)
다음 표는 사용자가 넣을 수 있는 입력의 종류를 나타낸다.
 
문자	동작
U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.



'''
