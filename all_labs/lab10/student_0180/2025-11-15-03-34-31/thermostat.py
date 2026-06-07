# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp = 68):
        self.temp = temp
        self.schedule = {}

    def add_schedule(self, time, temp):
        self.schedule[time] = temp

    def __str__(self):
        res = f"Default temperature: {self.temp} degrees"
        
        if not self.schedule:
            return res
        for t in sorted(self.schedule):
            temp = self.schedule[t]
            res += f"\n{t} {temp} degrees"
        
        return res
    
    def get_target_temperature(self, query_time):
        if not self.schedule:
            return self.temp
        times = sorted(self.schedule)
        if query_time < times[0]:
            return self.temp
        
        latest_time = None
        for t in times:
            if t <= query_time:
                latest_time = t
            else:
                break
        
        if latest_time is None:
            return self.temp
        
        return self.schedule[latest_time]