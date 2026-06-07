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
        target_temp = self.default_temperature 
        sorted_schedules = sorted(self.schedules.items())
        for scheduled_time, temperature in sorted_schedules:
            if scheduled_time <= query_time:
                target_temp = temperature 
            else:
                break
   
        return target_temp







      

    