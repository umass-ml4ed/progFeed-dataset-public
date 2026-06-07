# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        result = "Default temperature: " + str(self.default_temp) + " degrees"
        if len(self.schedules) == 0:
            return result

        for time in sorted(self.schedules):
            result += "\n" + time + " " + str(self.schedules[time]) + " degrees"

        return result

    def get_target_temperature(self, query_time):
        if len(self.schedules) == 0:
            return self.default_temp

        times = sorted(self.schedules)

        if query_time < times[0]:
            return self.default_temp

        latest = None
        for t in times:
            if t <= query_time:
                latest = t
            else:
                break

        if latest is not None:
            return self.schedules[latest]

        return self.default_temp