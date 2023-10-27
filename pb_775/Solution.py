def	num_slot(S):
	start_time = sorted(interval[0] for interval in S)
	end_time = sorted(interval[1] for interval in S)
	start_i = 0
	end_i = 0
	amounts = 0
	while start_i < len(S):
		if start_time[start_i] < end_time[end_i]:
			amounts += 1
			start_i += 1
		else:
			end_i += 1
			start_i += 1
	return (amounts)
# S = [(30, 75), (0, 50), (60, 150)]
# S = [(0, 1), (2, 3), (4, 5)]
S = [(0, 10), (1, 3), (2, 5), (6, 7), (4, 11)]
print(num_slot(S))