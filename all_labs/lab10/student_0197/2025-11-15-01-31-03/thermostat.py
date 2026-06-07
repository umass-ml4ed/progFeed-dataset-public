# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
	def_temp = 68
	schedules = {}
	def __init__(self, default= 68):
		self.def_temp = default

	def add_schedule(self, time, temp):
		self.schedules[time] = temp

	def __str__(self):
		fin = "Default temperature: " + str(self.def_temp) + " degrees"
		if self.schedules:
			for i in sorted(self.schedules):
				fin = fin + "\n" + i + " " + str(self.schedules[i]) + " degrees"
		return fin

	#def get_target_temperature(self, query):
	#	Tempor = "25:00"
	#	sorted_sched = sorted(self.schedules)
	#	if not sorted_sched:
	#		retun self.def_temp
	#	for i in sorted_sched:
	#		if i > query:
	#			return self.schedules[Tempor]
	#		Tempor = i
	#	return self.schedules[Tempor]


#tester = Thermostat()
#tester.add_schedule('19:35', 75.5)
#tester.add_schedule('08:00', 60.4)
#tester.add_schedule('22:39', 68.2)
#print(tester)