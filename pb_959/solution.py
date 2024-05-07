# def setbits(value):
# 	count = 0
# 	while value != 0:
# 		if value % 2 == 1:
# 			count += 1
# 		value //= 2
# 	return count

def setbits(value):
	count = 0
	while value:
		count += value & 1
		value >>= 1
	return count

def Allsetbits(N):
	sum = 0
	for i in range(N + 1):
		sum += setbits(i)
	return sum

print(Allsetbits(3))