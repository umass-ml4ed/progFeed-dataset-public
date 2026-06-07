# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __innit__(self, temp=68):
        self.temp = temp
        self.schedule = {}
    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature
    def __str__():
