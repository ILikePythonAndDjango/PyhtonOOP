from datetime import datetime
import sys
from abc import ABCMeta, abstractmethod

class AbsctractTimeAmount(metaclass=ABCMeta):

	@abstractmethod
	def get_length(self):
		pass

	def enough_for(self, another_delta):
		return self.get_length >= another_delta

class TimeInterval():
	DEFAULT_BEGIN = datetime(1970, 1, 1)

	def __init__(self, begin=None, end=None):
		if begin is None:
			begin = self._get_default_begin()
		if end is None:
			end = self._get_default_end()

		self._begin = begin
		self._end = end

	def __repr__(self):
		return "{namespace}.TimeInterval(begin='{begin}', end='{end}')".format(
			namespace = __name__,
			begin = self._begin,
			end = self._end
		)

	def __str__(self):
		return "{} -> {}".format(self._begin, self._end)

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
	print()
	print(repr(interval))
	print(interval)