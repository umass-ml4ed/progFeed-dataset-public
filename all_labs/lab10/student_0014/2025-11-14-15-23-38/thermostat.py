# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat():
    def __init__ (self, def_temp = 68):
        self.def_temp = def_temp
        self.schedules = {}
    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature
        
