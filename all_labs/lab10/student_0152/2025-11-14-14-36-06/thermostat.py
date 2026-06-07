# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp = 68):
        self.temp = temp
        temps = {}
    def add_schedule(self, time, temp):
        self.temp[time] = temp