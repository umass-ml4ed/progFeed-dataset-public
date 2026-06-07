# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temperature=68):
        self.default_temperature = default_temperature
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature
        

