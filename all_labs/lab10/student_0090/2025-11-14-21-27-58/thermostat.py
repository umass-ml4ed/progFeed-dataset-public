# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, initial_temp=68):
        self.current_temp = initial_temp
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        result = f"Default temperature: {self.current_temp} degrees"
        
        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"
        
        return result
    
    def get_target_temp(self, time):
        return self.schedules.get(time, self.current_temp)
    
    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.current_temp
        
        sorted_times = sorted(self.schedules.keys())
        
        target_time = None
        for sched_time in sorted_times:
            if sched_time <= query_time:
                target_time = sched_time
            else:
                break
        
        if target_time is None:
            return self.current_temp
        
        return self.schedules[target_time]