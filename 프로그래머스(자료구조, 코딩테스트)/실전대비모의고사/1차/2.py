def solution(want, number, discount):
	answer = 0
	want_dict = {k: v for k, v in zip(want, number)}
	
	compare_dict = dict()
	for k in discount[:10]:
		compare_dict[k] = compare_dict.get(k, 0) + 1
	
	if want_dict == compare_dict:
		answer += 1
	
	for i in range(10, len(discount)):
		item = discount[i]
		before_item = discount[i - 10]
		
		compare_dict[item] = compare_dict.get(item, 0) + 1
		if compare_dict.get(before_item):
			compare_dict[before_item] = compare_dict[before_item] - 1
			
			if compare_dict[before_item] == 0:
				del compare_dict[before_item]
		
		if want_dict == compare_dict:
			answer += 1
	
	return answer

solution(
	["banana", "apple", "rice", "pork", "pot"],
	[3, 2, 2, 2, 1],
	["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple",
	 "banana"])