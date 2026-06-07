# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp=68):
        self.temp = temp
        self.sched = {}
    def add_schedule(self, time, temperature):
        self.sched[time] = temperature
