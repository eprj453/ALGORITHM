def mergeSort(arr, p, r):
    q = int((p + r) / 2)
    # print("p : {}, r : {}, q : {}".format(p, r, q))
    if p < r:
        mergeSort(arr, p, q)
        mergeSort(arr, q+1, r)
        return merge(arr, p, q, r)
    else:
        return arr

def merge(arr, p, q, r):
    i = p # 첫번째 배열 시작
    j = q+1 # 첫번째 배열 끝
    k = 0 # 두번째 배열 시작
    temp = [0] * (r-p+1)

    while i <= q and j <= r:
        print("p : {}, r : {}, q : {}".format(p, r, q))
        print('i : {} , j : {}, len_arr : {}'.format(i, j , len(arr)))
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1

    while i <= q:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= r:
        temp[k] = arr[j]
        k += 1
        j += 1

    for x in range(r-p+1):
        arr[p+x] = temp[x]

    return arr

arr1 = [6,5,4,3,2,1]
print(mergeSort(arr1, 0, len(arr1)-1))