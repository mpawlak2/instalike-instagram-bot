import datetime
from random import randint

class PeriodRandomizer:
	def __init__(self):
		# 0 - 23 format
		self.from_hour = 12
		self.to_hour = 23

		self.from_time = None
		self.to_time = None

		self.work_for = 6 * 60 # means bot will be working for a total of # minutes

		# periods
		self.min_periods = 2
		self.max_periods = 4

		# in minutes
		self.min_period_length = 30
		self.max_period_length = 0
		self.actual_length = 0

		self.periods = []

	def randomize(self):
		self.periods = []

		now = datetime.datetime.now()
		self.from_time = datetime.datetime(now.year, now.month, now.day, self.from_hour)
		self.to_time = datetime.datetime(now.year, now.month, now.day, self.to_hour)

		minute_len = (self.to_time - self.from_time).seconds / 60
		if (self.work_for > minute_len):
			self.periods.append(Period(self.from_time, self.to_time)) # work whole time
			return

		no_of_periods = randint(self.min_periods, self.max_periods)
		while(len(self.periods) < no_of_periods):
			start_minute = randint(0, minute_len)
			period_len = randint(self.min_period_length, self.work_for / (no_of_periods - 1))
			if (len(self.periods) == no_of_periods - 1):
				period_len = self.work_for - self.actual_length

			if (period_len < self.min_period_length):
				period_len = self.min_period_length

			start_here = self.from_time + datetime.timedelta(minutes = start_minute)
			stop_here = self.from_time + datetime.timedelta(minutes = start_minute + period_len)

			# if (((self.to_time - stop_here).seconds / 60) < self.min_period_length):
			# 	continue
			# if (((start_here - self.from_time).seconds / 60) < self.min_period_length):
			# 	continue

			period_proposition = Period(start_here, stop_here)

			if (len(self.periods) == 0):
				self.periods.append(period_proposition)
				self.actual_length += period_proposition.get_length()
				continue

			valid = True
			for period in self.periods:
				if (period_proposition.during(period)):
					valid = False
					break

			if (valid):
				self.periods.append(period_proposition)
				self.actual_length += period_proposition.get_length()

	def is_active(self):
		for period in self.periods:
			if (period.is_active()):
				return True

		return False

	def info(self):
		for period in self.periods:
			period.get_times()
		print(self.actual_length)


		
class Period:
	def __init__(self, from_time, to_time):
		self.start_time = from_time
		self.end_time = to_time

	def is_active(self):
		now = datetime.datetime.now()
		if (now > self.start_time and now < self.end_time):
			return True
		return False

	def during(self, period):
		if (self.start_time >= period.start_time and self.start_time <= period.end_time):
			return True
		if (self.end_time >= period.start_time and self.end_time <= period.end_time):
			return True
		if (self.start_time <= period.start_time and self.end_time >= period.end_time):
			return True
		return False

	def get_length(self):
		return (self.end_time - self.start_time).seconds / 60

	def get_times(self):
		print('from {0} to {1}, minutes: {2}, active: {3}'.format(self.start_time, self.end_time, self.get_length(), self.is_active()))