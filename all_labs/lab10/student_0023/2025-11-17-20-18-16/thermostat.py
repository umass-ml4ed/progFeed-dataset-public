# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        lines = []
        lines.append(f"Default temperature: {self.default_temp} degrees")
        for t in sorted(self.schedules):
            lines.append(f"{t} {self.schedules[t]} degrees")
        return "\n".join(lines)

    def get_target_temperature(self, query_time):
        latest_time = None
        for t in sorted(self.schedules):
            if t <= query_time:
                latest_time = t
            else:
                break
        if latest_time is None:
            return self.default_temp
        return self.schedules[latest_time]
