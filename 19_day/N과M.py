arr = 'ABC'

N = len(arr)

for i in range(N): # 중복순열
    for j in range(N):
        if i == j: continue
        for k in range(N):
            if i == k or j == k: continue
            print(arr[i], arr[j], arr[k])