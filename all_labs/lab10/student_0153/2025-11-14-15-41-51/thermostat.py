# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}
    
    def add_schedule(self, time, temp):
        self.schedules[time] =temp
    
    def __str__(self):
        result = "Default temperature: " + str(self.default_temp) + " degrees"
        for time in sorted(self.schedules):
            temp = self.schedules[time]
            result = result + "\n" + time + " " + str(temp) + " degrees"
        
        return result
    
    def get_target_temperature(self, Qtime):
        if len(self.schedules) == 0:
            return self.default_temp
        latest_time = None
        for time in sorted(self.schedules):
            if time <= Qtime:
                latest_time = time
            else:
                break
        if latest_time == None:
            return self.default_temp
        return self.schedules[latest_time]