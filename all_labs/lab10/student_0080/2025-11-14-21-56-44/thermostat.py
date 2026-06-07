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
        if self.schedules:
            sorted_times = sorted(self.schedules.keys())
            for time in sorted_times:
                result += f"\n{time} {self.schedules[time]} degrees"
        
        return result

    def get_target_temperature(self, query_time):

        if not self.schedules:
            return self.default_temp
        
        valid_times = [time for time in self.schedules.keys() if time <= query_time]
        
        if not valid_times:
            return self.default_temp
        else:
            latest_time = max(valid_times)
            return self.schedules[latest_time]