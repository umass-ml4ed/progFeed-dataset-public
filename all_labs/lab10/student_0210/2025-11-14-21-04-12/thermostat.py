# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, temp=68):
        self.temp = temp
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        output = output = f"Default temperature: {self.temp} degrees"
        if self.schedules:
            sortedTimes = sorted(self.schedules)
            for t in sortedTimes:
                output += f"\n{t} {self.schedules[t]} degrees"
        return output

    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.temp
        sorted_times = sorted(self.schedules)
        for t in reversed(sorted_times):
            if query_time >= t:
                return self.schedules[t]
        return self.temp