ans = 0xffffff
def swap(s1, s2, arr, cnt, K):
    global ans
    # print(arr)
    if cnt >= ans: return
    for a in range(len(arr)-1):
        if abs(arr[a+1] - arr[a]) > K:
            break
    else:
        ans = min(ans, cnt)
        return

    for i in range(s1, len(arr)-1):
        for j in range(s2, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            swap(s1, s2+1, arr, cnt+1, K)
            arr[j], arr[i] = arr[i], arr[j]
        # swap(s1+1, s2, arr, cnt+1, K)

swap(0, 1, [3, 7, 2, 8, 6, 4, 5, 1], 0, 3)
print(ans)