# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        lines = [f"Default temperature: {self.default_temp} degrees"]
        for t in sorted(self.schedules.keys()):
            lines.append(f"{t} {self.schedules[t]} degrees")
        return "\n".join(lines)

    def get_target_temperature(self, query_time):
        target = self.default_temp
        for t in sorted(self.schedules.keys()):
            if t <= query_time:
                target = self.schedules[t]
            else:
                break
        return target

