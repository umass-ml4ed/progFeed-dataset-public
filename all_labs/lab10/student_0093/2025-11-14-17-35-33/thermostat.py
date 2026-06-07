# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, temp = 68):
        self.temp = temp
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        result = "Default temperature: " + self.temp + " degrees"
        for time in sorted(self.schedules):
            temp = self.schedules[time]
            result.append(time + temp + " degrees")
        return "\n".join(result)