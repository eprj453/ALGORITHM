# pivot item(기준 아이템)을 중심으로 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.

# quick sort는 최소 nlogn, 최대 n^2의 시간복잡도를 가질 수 있다.


def partition(arr, l, r):
    pivot = arr[l]
    # print('pivot : {}번째 원소 {}'.format(l ,arr[l]))
    i = l + 1
    j = r
    while i <= j:
        while i <= j and arr[i] <= pivot:
            # print('i 증가 {}번째 원소 {}'.format(i, arr[i]))
            i += 1
        while i <= j and arr[j] >= pivot:
            # print('j 감소 {}번째 원소 {}'.format(j, arr[j]))
            j -= 1
        if i <= j:
            # print('i: {}번째 {}와 j: {}번째 {} 교환'.format(i, arr[i], j, arr[j]))
            arr[i], arr[j] = arr[j], arr[i]
    # print('l: {}번째 {}와 j: {}번째 {} 교환'.format(l, arr[l],j, arr[j]))
    arr[l], arr[j] = arr[j], arr[l]
    # print('arr : ',arr)
    return j
def quickSort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quickSort(arr, l, s-1)
        quickSort(arr, s+1, r)

for i in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    quickSort(arr, 0, n-1)
    print('#{} {}'.format(i, arr[n//2]))
