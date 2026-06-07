# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp = 68):
        self.default_temp = default_temp
        self.schedules = {}
    def add_schedule(self, time, temprature):
        self.schedules[time] = float(temprature)
    def __str__(self):
        output = ""
        if len(self.schedules) == 0:
            output += f'Default temperature: {float(self.default_temp)} degrees'
        for time in sorted(self.schedules):
            output += f'\n {time} {float(self.schedules[time])} degrees'
        return output
    def get_target_temprature(self, query):
        sorted_time = sorted(self.schedules)
        for time in sorted_time:
            if time <= query:
                latest_time = time
        if latest_time == None:
           return self.default_temp
        return self.schedule[latest_time]
            
       

