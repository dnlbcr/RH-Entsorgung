from datetime import datetime

class GarbageCollection:
	def __init__(self, date, container):
		self.date = date
		self.container = container

	def __str__(self):
		return self.date.strftime("%Y/%m/%d") + ' ' + self.container + ' ' + self.interval 