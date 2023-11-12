def max_multiply(numbers):
	pos = list()
	neg = list()
	for e in numbers:
		if e >=0:
			pos.append(e)
		else:
			neg.append(e)
	pos.sort()
	neg.sort()
	if len(neg) == 0:
		res = pos[-1] * pos[-2] * pos[-3]
	elif len(pos) == 0:
		res = neg[-1] * neg[-2] * neg[-3]
	else:
		res = max(neg[0] * neg[1] * pos[-1], pos[-1] * pos[-2] * pos[-3])
	return res
numbers = [int(e) for e in input().strip().split()]
print(max_multiply(numbers))