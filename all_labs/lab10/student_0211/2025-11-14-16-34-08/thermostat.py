# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp = 68):
        self.default_temp = default_temp
        self.schedules = {}
    def add_schedule(self, time, temperature):
        self.schedules[time] = float(temperature)

    def __str__(self):
        output = f'Default temperature: {self.default_temp} degrees'
        for time in sorted(self.schedules):
            output += f'\n{time} {self.schedules[time]} degrees'
        return output
    
    def get_target_temperature(self, query):
        sorted_time = sorted(self.schedules)
        latest_time = None
        for time in sorted_time:
            if time <= query:
                latest_time = time
        if latest_time == None:
           return self.default_temp
        return self.schedules[latest_time]
            
       

