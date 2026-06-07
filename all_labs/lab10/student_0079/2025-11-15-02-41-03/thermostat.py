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
        output = f"Default temperature: {self.default_temp} degrees"
        if len(self.schedules) == 0:
            return output
        output += "\n"
        times = sorted(self.schedules)
        for i, t in enumerate(times):
            temp = self.schedules[t]
            if i == len(times) - 1:
                output += f"{t} {temp} degrees"
            else:
                output += f"{t} {temp} degrees\n"
        return output

    def get_target_temperature(self, query_time):
        times = sorted(self.schedules)
        if len(times) == 0:
            return self.default_temp
        if query_time < times[0]:
            return self.default_temp
        temp = self.default_temp
        for t in times:
            if t <= query_time:
                temp = self.schedules[t]
            else:
                break
        return temp