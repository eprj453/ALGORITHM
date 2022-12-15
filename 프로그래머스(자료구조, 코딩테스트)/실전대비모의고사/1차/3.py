def solution(order):
	answer = 0
	order_idx = 0
	
	second_container = []
	delivery = [i for i in range(1, len(order) + 1)]
	truck = []
	for d in delivery:
		
		if d == order[order_idx]:
			truck.append(d)
			order_idx += 1
			if second_container and second_container[-1] == order[order_idx]:
				truck.append(second_container.pop())
				order_idx += 1
		
		elif second_container and second_container[-1] == order[order_idx]:
			truck.append(second_container.pop())
			order_idx += 1
			if d == order[order_idx]:
				truck.append(d)
				order_idx += 1
		else:
			second_container.append(d)
	
	print(second_container)
	while second_container:
		item = second_container.pop()
		if item == order[order_idx]:
			truck.append(item)
			order_idx += 1
		else:
			break
		# print('while')
	answer = len(truck)
	# print(truck)
	# print(answer)
	print(truck)
	return answer


a = solution([1, 3, 2, 4, 6, 7, 5, 8])

print(a)
