import copy

def rotate90(array):
    n = len(array)
    arr = [[0] * n for _ in range(n)]
    i2, j2 = 0, 0
    for i in range(n):
        for j in range(n-1, -1, -1):
            arr[i2][j2] = array[j][i]
            j2 += 1
        j2 = 0
        i2 += 1
    return arr

def check_unlock(key, lock):
    n, m = len(key), len(lock)
    start = len(key)-1
    end = m - (n-1)

    for i in range(0, m-n):
        for j in range(0, m-n):
            copy_lock = copy.deepcopy(lock)
            # print(i, j)
            for k in range(0, n):
                for l in range(0, n):
                    # print(i, k, j, l)
                    copy_lock[i+k][j+l] += key[k][l]
            # for g in range(m):
                # print(copy_lock[g])
            flag = True
            for k in range(start, end):
                for l in range(start, end):
                    if copy_lock[k][l] != 1:
                        flag = False
                        break
            if flag:
                return True
    return False


def solution(key, lock):
    answer = False
    rotate_count = 0
    lock_len = len(lock)
    for _ in range(len(key)-1):
        for l in lock:
            l.insert(0, 0)
            l.append(0)

    for _ in range(len(key)-1):
        temp = [0] * (lock_len + ((len(key) - 1) * 2))
        lock.insert(0, temp)
        lock.append(temp)


    while rotate_count < 4:
        if check_unlock(key, lock):
            answer = True
            break
        else:
            key = rotate90(key)
            rotate_count += 1

    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	))