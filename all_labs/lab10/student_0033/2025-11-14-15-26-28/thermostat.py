# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temperature=68):
        self.default_temperature = default_temperature
        self.schedules = {}
    
    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature
    
    def __str__(self):
 
        result = f"Default temperature: {self.default_temperature} degrees"
        
        sorted_times = sorted(self.schedules)
        for time in sorted_times:
            temperature = self.schedules[time]
            result += f"\n{time} {temperature} degrees"
        
        return result
    
    def get_target_temperature(self, query_time):
      
        if not self.schedules:
            return self.default_temperature
        
       
        sorted_times = sorted(self.schedules.keys())
        
    
        target_time = None
        for schedule_time in sorted_times:
            if schedule_time <= query_time:
                target_time = schedule_time
            else:
                break
        
        if target_time is None:
            return self.default_temperature
        
        return self.schedules[target_time]
