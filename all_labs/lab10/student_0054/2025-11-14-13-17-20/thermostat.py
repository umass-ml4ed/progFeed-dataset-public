# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        result = "Default temperature: " + str(self.default_temp) + " degrees"
        times = sorted(self.schedules.keys())
        for t in times:
            result = result + "\n" + t + " " + str(self.schedules[t]) + " degrees"
        return result
    
    def get_target_temperature(self, query_time):
        if len(self.schedules) == 0:
            return self.default_temp
        times = sorted(self.schedules.keys())
        last_temp = None
        for t in times:
            if t <= query_time:
                last_temp = self.schedules[t]
            else:
                break
        if last_temp is None:
            return self.default_temp
        else:
            return last_temp
