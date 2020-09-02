n, m = map(int, input().split())
dduk_list = list(map(int, input().split()))

start = 1
end = 2000000000
answer = 0

while start <= end:
    mid = (start + end) // 2
    print('mid : ',mid)
    cut = 0
    for d in dduk_list:
        if d > mid:
            cut += (d - mid)
    # if cut == m: break
    if cut > m: # 가져가는 떡이 많을 경우 -> mid를 올려도 됨(여유있음)
        start = mid + 1
        # answer = cut
    else:
        end = mid - 1 # 가져가는 떡이 너무 적음 -> 더 가져갈수 있음
        answer = mid

print(answer)

