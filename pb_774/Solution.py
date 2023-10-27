class FileReader:
	def __init__(self, filepath):
		self.filepath = filepath
		self.f = open(filepath, mode='r')
	def read7(self):
		return(self.f.read(7))
	def readN(self, n):
		buffer = ""
		result = ""
		while n > 0:
			buffer = self.f.read(7)
			if not buffer:
				return result
			else:
				if n > 7:
					result += buffer
					n -= 7
				else:
					result += buffer[0:n]
					n = 0
		return result
filereader = FileReader("a.txt")
print(filereader.readN(100))
# print(filereader.read7())
# print(filereader.read7())