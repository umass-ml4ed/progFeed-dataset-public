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
        out = f"Default temperature: {self.default_temp} degrees"
        keys = sorted(self.schedules)
        for t in keys:
            out += f"\n{t} {self.schedules[t]} degrees"
        return out

    def get_target_temperature(self, query_time):
        keys = sorted(self.schedules)
        last_temp = None
        for t in keys:
            if t <= query_time:
                last_temp = self.schedules[t]
            else:
                break
        if last_temp is None:
            return self.default_temp
        return last_temp