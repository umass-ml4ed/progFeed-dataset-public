# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = float(default_temp)
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = float(temperature)

    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"
        for t in sorted(self.schedules):
            result += f"\n{t} {self.schedules[t]} degrees"
        return result

    def get_target_temperature(self, query_time):
        # sorted times in ascending order
        sorted_times = sorted(self.schedules)
        target_temp = self.default_temp
        for t in sorted_times:
            if query_time >= t:
                target_temp = self.schedules[t]
            else:
                break
        return target_temp



