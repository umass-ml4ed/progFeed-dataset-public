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
        result = f"Default temperature: {self.default_temp} degrees"
        times = sorted(self.schedules)
        for t in times:
            result += f"\n{t} {self.schedules[t]} degrees"
        return result

    def get_target_temperature(self, query_time):
        if len(self.schedules) == 0:
            return self.default_temp
        times = sorted(self.schedules)
        if query_time < times[0]:
            return self.default_temp
        last_time = times[0]
        for t in times:
            if t <= query_time:
                last_time = t
            else:
                break
        return self.schedules[last_time]
