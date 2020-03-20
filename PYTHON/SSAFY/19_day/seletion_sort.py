arr = [9, 2, 3, 7, 5, 6, 8, 1, 4, 10]

def getMin(s, e): # 최소값 구하기
    if s == e:
        return arr[s]
    else:
        ret = getMin(s, e-1)
        return min(ret, arr[e])

print(getMin(0, len(arr)-1))