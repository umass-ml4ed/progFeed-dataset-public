# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:


    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}
    def add_schedule(self, time, temp):
        self.schedules[time] = temp
    def __str__(self, default_temp= 68): 
        result = f"Default Temperature: {default_temp} degrees"
        sorted_times = sorted(self.schedules)
        for time in sorted_times: 
            result += f"\n{time} {self.schedules[time]} degrees"
        return result
        
    def get_target_temperature(self, query_time):
        if not self.schedules: 
            return self.default_temp
        sorted_times = sorted(self.schedules)
        target_time = None
        for time in sorted_times:
            if time <= query_time:
                target_time = time
            else:
                break
        if target_time is None:
            return self.default_temp
        return self.schedules[target_time]






    

    
    

    
