def solution(clothes):
    answer = 0
    clothDict = {}
    for cloth in clothes:
        thing, category = cloth[0], cloth[1]
        clothDict[category] = clothDict.get(category, 0) + 1

    # nums = []
    for value in clothDict.values():
        answer += (value+1)
    answer -= 1




        # for key in clothDict.keys():
        #     if category != key:
        #         answer += len(clothDict[key])
        #
        # if clothDict.get(category) == None:
        #     clothDict[category] = [thing]
        # else:
        #     clothDict[category].append(thing)
        # answer += 1
        # print(clothDict)

    return answer

# print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))