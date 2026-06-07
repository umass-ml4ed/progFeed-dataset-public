# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time_str, temp):
        self.schedules[time_str] = temp

    def __str__(self):
        result = "Default temperature: " + str(self.default_temp) + " degrees"
        if len(self.schedules) == 0:
            return result
        times = sorted(self.schedules)
        for t in times:
            result = result + "\n" + t + " " + str(self.schedules[t]) + " degrees"
        return result

    def get_target_temperature(self, query_time):
        if len(self.schedules) == 0:
            return self.default_temp
        times = sorted(self.schedules)
        latest = None
        for t in times:
            if t <= query_time:
                latest = t
        if latest is None:
            return self.default_temp
        return self.schedules[latest]