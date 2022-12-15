def solution(X, Y):
	answer = ''
	x, y = sorted(list(X)), sorted(list(Y))
	
	x_pointer, y_pointer = 0, 0
	
	pairs = []
	
	while x_pointer < len(X) and y_pointer < len(Y):
		x_value, y_value = x[x_pointer], y[y_pointer]
		
		if x_value == y_value:
			pairs.append(x_value)
			x_pointer += 1
			y_pointer += 1
		elif x_value > y_value:
			y_pointer += 1
		else:
			x_pointer += 1
	
	pairs.sort(reverse=True)
	
	if not pairs:
		return '-1'
	elif pairs[0] == '0':
		return '0'
	else:
		return ''.join(pairs)


a = solution('100', '123450')
print(a)