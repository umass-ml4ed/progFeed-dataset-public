# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp = 68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

def __str__(self):
    all_lines = []
    all_lines.append(f"Default temperature: {self.default_temp} degrees")
    for time in sorted(self.schedules):
        temp = self.schedules[time]
        schedule_line = f"{time} {temp} degrees"
        all_lines.append(schedule_line)
    return  "\n".join(all_lines)

