from collections import namedtuple
from sys import getsizeof
from datetime import datetime

class TimeInterval(namedtuple("TimeInterval", ('begin', 'end'))):
	def get_length(self):
		return self.end - self.begin

	def __repr__(self):
		return "{namespace}.TimeInterval(begin='{begin}', end='{end}')".format(
			namespace = __name__,
			begin = self.begin,
			end = self.end
		)

	def __str__(self):
		return "{} -> {}".format(self._begin, self._end)

interval = TimeInterval(datetime(2018, 1, 1), datetime(2018, 1, 2))
for d in dir(interval):
	print(d)
print()
print(interval.begin)
print(interval.end)
print(getsizeof(interval))
print(interval.get_length())
print('count', interval.count(datetime(2018, 1, 1)))
print('index', interval.index(datetime(2018, 1, 1)))