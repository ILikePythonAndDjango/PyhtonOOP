from datetime import datetime
import sys

class TimeInterval:
	DEFAULT_BEGIN = datetime(1970, 1, 1)

	def __init__(self, begin=None, end=None):
		if begin is None:
			begin = self._get_default_begin()
		if end is None:
			end = self._get_default_end()

		self._begin = begin
		self._end = end

	@classmethod
	def _get_default_begin(cls):
		return cls.DEFAULT_BEGIN

	@staticmethod
	def _get_default_end():
		return datetime.now()

	@property
	def begin(self):
		return self._begin

	@begin.setter
	def begin(self, value):
		self._begin = value

	@property
	def end(self):
		return self._end

	@end.setter
	def end(self, value):
		self._end = value

if __name__ == '__main__':
	interval = TimeInterval()
	print(interval._begin)
	print(interval._end)
	print(sys.getsizeof(TimeInterval), sys.getsizeof(interval))
	interval.begin = datetime(2000, 10, 31)
	interval.end = datetime(2005, 10, 31)
	print(interval.begin)
	print(interval.end)