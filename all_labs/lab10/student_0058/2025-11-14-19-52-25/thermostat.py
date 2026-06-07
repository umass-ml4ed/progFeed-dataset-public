# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat():
    def __init__(self, n = 68):
        self.n = n
        self.schedules = {}

    def add_schedule(self,time:str, temp:float):
        self.schedules[time] = temp

    def __str__(self):
        result = f"Default temperature: {self.n} degrees"

        if not self.schedules:
            return result
        
        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"
        return result 