arr = [60,80,11,65,32]

# 최소값의 위치를 찾는다.

for j in range(0, len(arr)):
    min_idx = j
    for i in range(min_idx+1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    arr[j], arr[min_idx] = arr[min_idx], arr[j]

print(arr)