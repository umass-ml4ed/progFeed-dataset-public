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
        if not self.schedules:
            return result
        for t in sorted(self.schedules):
            result += f"\n{t} {self.schedules[t]} degrees"
        return result

    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp
        
        times = sorted(self.schedules)
        latest = None
        
        for t in times:
            if t <= query_time:
                latest = t
            else:
                break
        
        if latest is None:
            return self.default_temp
        return self.schedules[latest]
