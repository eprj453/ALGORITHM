import math

def is_special_ch(string):
    for s in string:
        if not s.isalpha():
            return True
    return False


def exist_and_not_visited_index(visited, arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele and not visited[i]:
            return i
    return None

def get_intersection(arr1, arr2):
    intersection = []
    visited = [False] * len(arr2)

    for s in arr1:
        if s in arr2:
            get_idx = exist_and_not_visited_index(visited, arr2, s)
            if get_idx is not None:
                intersection.append(arr2[get_idx])
                visited[get_idx] = True

    return intersection

def get_union(arr1, arr2):
    union = []
    visited = [False] * len(arr2)

    for s in arr1:
        if s in arr2:
            get_idx = exist_and_not_visited_index(visited, arr2, s)
            if get_idx is not None:
                visited[get_idx] = True
        union.append(s)

    for idx, boolean in enumerate(visited):
        if not boolean:
            union.append(arr2[idx])

    return union

def make_set(string):
    ele_set = []
    n = len(string)
    for i in range(n-1):
        ele = string[i:i+2]
        if not is_special_ch(ele) and len(ele) == 2:
            ele_set.append(ele.lower())

    return ele_set

def calculate_jaccard_similarity(set1, set2):
    inter = get_intersection(set1, set2)
    union = get_union(set1, set2)
    if not inter and not union:
        return 1
    return len(inter) / len(union)


def solution(str1, str2):
    answer = 0
    set1, set2 = make_set(str1), make_set(str2)
    answer = calculate_jaccard_similarity(set1, set2) * 65536
    return math.trunc(answer)