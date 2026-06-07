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
        result = f"Default temperature: {self.default_temp} degrees"
        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"
        return result
    
    
    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp
        sorted_times = sorted(self.schedules)
        latest_time = None
        for time in sorted_times:
            if time <= query_time:
                latest_time = time
            else:
                break
        if latest_time is None:
            return self.default_temp
        return self.schedules[latest_time]