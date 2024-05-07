from collections import deque

class orderlogs:
	def __init__(self, N):
		self.N = N
		self.log = deque()
	def record(self, order_id):
		if (len(self.log) == self.N):
			self.log.popleft()
		self.log.append(order_id)
	def get_last(self, i):
		if i <= len(self.log):
			return self.log[-i]
		else:
			None
	# def get_last_i(self, i):
	# 	if i <= len(self.log):
	# 		return list(self.log)[-i:]
	# 	else:
	# 		None

orderlog = orderlogs(5)
orderlog.record(1)
orderlog.record(2)
orderlog.record(3)
orderlog.record(4)
orderlog.record(5)
orderlog.record(6)
orderlog.record(7)
print("list of item:")
for item in orderlog.log:
	print(item)
print("get last:")
print(orderlog.get_last(2))
print(orderlog.get_last(7))
# print("get last i:")
# print(orderlog.get_last_i(3))