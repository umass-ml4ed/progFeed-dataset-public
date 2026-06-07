# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self,default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"
        times = sorted(self.schedules)
        for time in times:
            temp = self.schedules[time]
            result += f"\n{time} {temp} degrees"
        return result
    
    def get_target_temperature(self, query_time):
        times = sorted(self.schedules)
        if not times:
            return self.default_temp
        last_time = None
        for time in times:
            if time <= query_time:
                last_time = time
            else:
                break
        if last_time is None:
            return self.default_temp
        else:
            return self.schedules[last_time]