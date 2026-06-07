# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temperature = 68):
        self.temperature = temperature
        self.schedules = {}

    def add_schedule(self,time:str,temp:float):
        self.schedules[time] = temp

    def __str__(self):

        sorts = sorted(self.schedules)
        a = [f"Default temperature: {self.temperature} degrees"]
        for time in sorts:
            temp = self.schedules[time]
            a.append(f"{time} {temp} degrees")
        return "\n".join(a)
