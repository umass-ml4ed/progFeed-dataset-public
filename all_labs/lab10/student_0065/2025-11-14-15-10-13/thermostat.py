# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self,default_temperature = 68):
        self.default = default_temperature
        self.schedule = {}

    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature

    def __str__(self):
        lines = [f"Default temperature: {self.default} degrees"]
        for time in sorted(self.schedule):
            lines.append(f"{time} {self.schedule[time]} degrees")
        return "\n".join(lines)
