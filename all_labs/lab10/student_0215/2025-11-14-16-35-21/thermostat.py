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
        result = f'Default temperature: {self.default_temp} degrees'
        if not self.schedules:
            return result
        for time in sorted(self.schedules):
            temp = self.schedules[time]
            result += f'\n{time} {temp} degrees'
        return result
    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp
        latest = None
        for time in sorted(self.schedules):
            if time <= query_time:
                latest = time
            else:
                break
            if latest is None:
                return self.default_temp
            return self.schedules[latest]
    