length = int(input())
red = sorted(list(map(int, input().split())))
blue = sorted(list(map(int, input().split())))
yellow = sorted(list(map(int, input().split())))

start, end = 0, length
center = (round(start, 1)+round(end, 1)) / 2
red_center = (round(red[0], 1) + round(red[1], 1)) / 2

if red_center > center:
    end = red_center
    for i in range(2):
        if blue[i] > end:
            blue[i] = round(end - (blue[i] - end), 1)
        if yellow[i] > end:
            blue[i] = round(end - (blue[i] - end), 1)
else:
    start = red_center
    for i in range(2):
        if blue[i] < start:
            blue[i] = round(start + (start - blue[i]), 1)
        if yellow[i] < start:
            yellow[i] = round(start + (start - yellow[i]), 1)

center = (start + end) / 2
print('blue : ',blue[0], blue[1])
print('yellow : ',yellow[0],yellow[1])
if blue[0] != blue[1]:
    blue_center = (blue[0] + blue[1]) / 2

    if blue_center > center:
        end = blue_center
        for i in range(2):
            if yellow[i] > end:
                yellow[i] = round(end - (yellow[i] - end), 1)

    else:
        start = blue_center
        for i in range(2):
            if yellow[i] < start:
                yellow[i] = round(start + (start - yellow[i]), 1)

center = (start + end) / 2
if yellow[0] != yellow[1]:
    y_center = (yellow[0] + yellow[1]) / 2

    if y_center > center:
        end = y_center
    else:
        start = y_center
print('yellow : ',yellow[0],yellow[1])
print('length : ', start, end)
print(abs(start-end))
# print(blue)
# print(yellow)
# print(blue[0] == blue[1])
# print((blue[0]+blue[1])/2)
# start = red_center
#
# print(start)
# if blue[0] < start:
#     blue[0] = start + (start-blue[0])
# if yellow[0] < start:
#     yellow[0] = start + (start-yellow[0])
#
# if blue[0] != blue[1]:  # 같으면 접을 필요 없다.
#      blue_center = (round(blue[0], 1) + round(blue[1], 1)) / 2
#      if end - blue_center < blue_center - start:  #  파란 점 중앙이 끝과 더 가깝다면
#




# print(red)
# print(green)
# print(blue)