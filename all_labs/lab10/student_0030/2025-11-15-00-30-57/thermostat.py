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
        lines = [f"Default temperatures: {self.default_temp} degrees "]
        for t in sorted(self.schedules):
            lines.append(f"{t} {self.schedules[t]} degrees ")
        return "\n".join(lines)
    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp
        latest = None
        for x in sorted(self.schedules):
            if x <= query_time:
                latest = x
            else:
                break
        if latest is None: 
            return self.default_temp
        return self.schedules