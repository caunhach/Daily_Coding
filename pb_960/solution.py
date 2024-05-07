# list1 = [1, 3, 1, 2, 0, 1]
# list2 = [1, 5, 2, 0, 0, 0]
# def IsApproachEnd(list):
# 	tmp_i = 0
# 	for i in range(len(list)):
# 		if list[i] + i > tmp_i:
# 			tmp_i = list[i] + i
# 			print(i)
# 		if i == tmp_i and list[i] == 0:
# 			break
# 	if tmp_i >= len(list) - 1:
# 		return True
# 	else:
# 		return False
# print(IsApproachEnd(list1))
# print(IsApproachEnd(list2))

list1 = [1, 3, 1, 2, 0, 1]
list2 = [1, 0, 2, 0, 0, 0]
def IsApproachEnd(list):
	tmp_i = 0
	for i in range(len(list)):
		if i > tmp_i:
			return False
		tmp_i = max(tmp_i, list[i] + i)
	return True
print(IsApproachEnd(list1))
print(IsApproachEnd(list2))