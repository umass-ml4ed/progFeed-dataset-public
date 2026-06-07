# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:

    def __init__(self, initial=68):
        self.default_temp = initial
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"
        if not self.schedules:
            return result
        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"

        return result
    
    def get_target_temperature(self, time):
        for i in sorted(self.schedules, reverse=True):
            if time >= i:
                return self.schedules[i]
        return self.default_temp
    