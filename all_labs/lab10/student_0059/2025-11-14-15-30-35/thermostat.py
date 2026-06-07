# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __innit__(self, temp):
        self.temp = 68
        self.schedule = {}
        dev = Thermostat(75)
    
    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature
        dev = Thermostat(75)
        dev.add_schedule("08:00", 60.4)
        print (self.schedule)