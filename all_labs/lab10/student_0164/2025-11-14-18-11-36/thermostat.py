# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.defualt_temp = default_temp
        self.schedules = {}
    
    
    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature 

    def __str__(self):
       result = f"Default temperature: {self.defualt_temp} degrees"
       for time in sorted(self.schedules):
           result += f"\n{time} {self.schedules[time]} degrees"
       return result 
   
    def get_target_temperature(self, query_time):
        sorted_times = sorted(self.schedules)
        if not sorted_times:
            return self.default_temp
        if query_time < sorted[0]:
            return self.default_temp
        target_temp = self.defualt_temp
        for time in sorted_times:
            if query_time >= time:
                target_temp = self.schedules[time]
            else:
                break
      

    