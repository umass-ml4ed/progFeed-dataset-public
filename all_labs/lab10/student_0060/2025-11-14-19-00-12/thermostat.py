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
        result = f"Default temperature: {self.default_temp} degrees"
        sorted_times = sorted(self.schedules)
        for t in sorted_times:
            result += f"\n{t} {self.schedules[t]} degrees"
        return result

    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp
        sorted_times = sorted(self.schedules)
        latest_time = None
        for t in sorted_times:
            if t <= query_time:
                latest_time = t
            else:
                break
        if latest_time is None:
            return self.default_temp
        return self.schedules[latest_time]