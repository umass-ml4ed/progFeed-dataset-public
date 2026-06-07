# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__ (self, temperature=68):
        self.temperature = temperature
        self.schedule = {}
    def add_schedule (self, time, temp):
        self.schedule[time] = temp