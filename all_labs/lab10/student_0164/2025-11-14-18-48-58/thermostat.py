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
        if not self.schedules:
            return self.default_temp
        times = sorted(self.schedules)
        last_temp = self.defualt_temp
        for t in times:
            if t <= query_time:
                last_temp = self.schedules[t]
            else:
                break
        return last_temp


      

    