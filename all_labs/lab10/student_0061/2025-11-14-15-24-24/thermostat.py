# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}
    def add_schedule(self, time_str, temperature):
        self.schedules[time_str] = temperature
    def __str__(self):
        lines = [f"Default temperature: {self.default_temp} degrees"]
        if self.schedules:
            for t in sorted(self.schedules):
                lines.append(f"{t} {self.schedules[t]} degrees")
        return "\n".join(lines)
    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp
        sorted_times = sorted(self.schedules)
        last_matching = None
        for t in sorted_times:
            if t <= query_time:
                last_matching = t
            else:
                break
        if last_matching is None:
            return self.default_temp
        return self.schedules[last_matching]  