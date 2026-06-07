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
        if len(self.schedules) == 0:
            return result
        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"
        return result

    def get_target_temperature(self, query_time):
        if len(self.schedules) == 0:
            return self.default_temp
        times = sorted(self.schedules)
        if query_time < times[0]:
            return self.default_temp
        target_temp = None
        for t in times:
            if t <= query_time:
                target_temp = self.schedules[t]
            else:
                break
        if target_temp is None:
            return self.default_temp
        return target_temp
