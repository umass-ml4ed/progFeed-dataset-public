# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, num = 68 ):
        self.default = num
        self.schedules = {}
    def add_schedule(self, time, temp):
        self.schedules[time] = temp
    def __str__(self):
        final = f"Default temperature: {self.default} degrees"
        for i in sorted(self.schedules):
            final += f"\n{i} {self.schedules[i]} degrees"
        return final
    def get_target_temperature(self, query_time):
        times = sorted(self.schedules)
        defaulttime = None
        for i in times:
            if i <= query_time:
                defaulttime = i
            else:
                break
        if defaulttime is None:
            return self.default
        return self.schedules[defaulttime]





