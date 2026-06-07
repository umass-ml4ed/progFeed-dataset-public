# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, initial_temp=68):
        self.current_temp = initial_temp
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        result = f"Default temperature: {self.current_temp} degrees"
        
        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"
        
        return result