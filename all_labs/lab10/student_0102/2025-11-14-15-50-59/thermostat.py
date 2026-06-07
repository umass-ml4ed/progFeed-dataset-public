# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED
class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time_str, temperature):
        self.schedules[time_str] = temperature

    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"
        for time in sorted(self.schedules):
            temp = self.schedules[time]
            result += f"\n{time} {temp} degrees"
        return result
    
    def get_target_temperature(self, query_time):
        valid_times = [t for t in self.schedules if t <= query_time]
        if valid_times:  
            latest = max(valid_times)
            return self.schedules[latest]
        else:
            return self.default_temp