def binary_search_loop(array, target):
    start, end = 0, len(array)-1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1


def split_alphanum(string):
    num_start = len(string)
    for i in range(len(string)):
        if string[i].isnumeric():
            num_start = i
            break
    alpha = string[:num_start]
    number = int(string[num_start:]) if string[num_start:] else 0

    return alpha,number



def solution(registered_list, new_id):
    answer = ''
    registered_dict = dict()

    for registered_id in registered_list:
        alpha, number = split_alphanum(registered_id)
        registered_dict[alpha] = registered_dict.get(alpha, [])
        registered_dict[alpha].append(number)
    
    for k in registered_dict.keys():
        registered_dict[k].sort()
    
    new_id_alpha, new_id_number = split_alphanum(new_id)

    recommend_id = ''
    for i in range(new_id_number, 1000000):
        if binary_search_loop(
            registered_dict.get(new_id_alpha, []),
            i
            ) is None:
            recommend_id = new_id_alpha + str(i) if i != 0 else new_id_alpha
            break

    return recommend_id
    
a = solution(["cow10", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow2")
print(a)

