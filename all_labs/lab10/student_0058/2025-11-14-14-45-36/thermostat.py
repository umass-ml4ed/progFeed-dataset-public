# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat():
    def __inti__(self, n = 68):
        self.n = n
        self.schedules = {}

    def add_schedule(self,time:str, temp:float):
        self.schedules[time] = temp