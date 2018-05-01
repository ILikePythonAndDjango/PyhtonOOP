
class Stream(object):
	def get_name(self):
		return 1

class InputStream(Stream):
	def read(self):
		return 'text'

	def get_name(self):
		return 2

class OutputStream(Stream):
	def write(self, text):
		return True

class InputOutputStream(InputStream, OutputStream):
	pass

stream = InputStream()
print(stream.read())

for cls in InputOutputStream.__mro__:
	print(cls)