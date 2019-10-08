n, c = map(int, input().split()) # 집의 갯수, 공유기 갯수
house_list = []
for i in range(n):
    house_list.append(int(input()))
house_list.sort()

start = 1
end = house_list[-1]-1
max_far = 0

while start <= end:
    count = 1
    mid = (start + end) // 2
    house_start = house_list[0]
    for num in range(1, len(house_list)):
        if house_list[num] - house_start >= mid:
            count += 1
            house_start = house_list[num]
    if count >= c:
        max_far = mid
        start = mid + 1
    else:
        end = mid - 1

print(max_far)