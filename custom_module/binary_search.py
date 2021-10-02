def binary_search_recursive(array, target, start, end):
    # 맨 처음 start = 0, end = end of array index
    if start > end:
        return None

    mid = (start + end) // 2 # 중간 인덱스

    # 일치하는 데이터가 있을 경우 인덱스 반환
    if array[mid] == target:
        return mid

    elif array[mid] > target: # 목표로 하는 값이 중간값보다 작을 경우는 범위를 왼쪽으로 가져간다.
        return binary_search_recursive(array, target, start, mid-1)

    else: # 목표로 하는 값이 중간값보다 클 경우 범위를 오른쪽으로 가져간다.
        return binary_search_recursive(array, target, start+1, end)


def binary_search_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None