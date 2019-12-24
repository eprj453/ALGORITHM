arr = []
key = 123
low, high = 0, len(arr)-1

while low <= high:
    mid = (low + high) >> 1
    if arr[mid] == key:
        print('존재합니다. {}번째에'.format(mid))
        break
    if arr[mid] > key:
        high = mid - 1
    if arr[mid] < key:
        low = mid + 1



def binarySearch(arr, low, high, key):
    if low > high:
        return False
    mid = (low + high) >> 1
    if arr[mid] == key:
        return True
    if arr[mid] > key:
        return binarySearch(arr, low, mid-1, key)
    if arr[mid] < key:
        return binarySearch(arr, mid+1, low, key)

    return -1