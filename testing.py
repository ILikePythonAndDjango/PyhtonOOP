import unittest
from unittest.mathc import patch
from datetime import datetime

from example import TimeInterval

class TimeIntervalTestCase(unittest.TestCase):
	def SetUp(self):
		self._interval = TimeInterval(
			datetime(2017, 1, 1),
			datetime(2018, 1, 1)
		)

	def test_init(self):
		self.assertEqual(self._interval._begin, datetime(2017, 1, 1))
		self.assertEqual(self._interval._end, datetime(2018, 1, 1))

	@patch('interval.datetime')
	def test_init__default(self, patched_datetime):
		patched_datetime.now.return_value = datetime(2018, 5, 1)
		interval = TimeInterval()
		self.assertEqual(interval._begin, datetime(1970, 1, 1))
		self.assertEqual(interval._end, datetime(2018, 5, 1))

	def test_str(self):
		self.assertEqual(
			str(self._interval),
			'2017-01-01 00:00:00 -> 2018-01-01 00:00:00'
		)