arr = [69, 19, 30, 2, 16, 8, 31, 22]
tmp = [0] * len(arr)

def mergeSort(lo, hi):
    global count
    if lo == hi: return
    mid = (lo + hi) >> 1 # 산술 shift (/= 2)
    mergeSort(lo, mid) # 왼쪽
    mergeSort(mid+1, hi) # 오른쪽
    i, j, k = lo, mid+1, lo
    # 왼쪽과 오른쪽을 병합
    print('left, right : ',arr[i], arr[j])

    if
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]
            j, k = j + 1, k + 1

    while i <= mid:
        tmp[k] = arr[i]
        i, k = i + 1, k + 1

    while j <= hi:
        tmp[k] = arr[j]
        j, k = j + 1, k + 1

    for i in range(lo, hi+1):
        arr[i] = tmp[i]

mergeSort(0, len(arr)-1)
print(arr)