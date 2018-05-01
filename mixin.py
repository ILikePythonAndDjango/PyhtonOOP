from datetime import datetime
from sys import getsizeof

class BeginEndMixin():
	DEFAULT_BEGIN = datetime(1970, 1, 1)

	@classmethod
	def _get_default_begin(cls):
		return cls.DEFAULT_BEGIN

	@staticmethod
	def _get_default_end():
		return datetime.now()

class TimeInterval(BeginEndMixin):
	__slots__ = ('_begin', '_end')

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

interval = TimeInterval()

print(interval)
print(getsizeof(interval))