# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp=68):
        self.temp=temp
        self.schedules={}

    def add_schedule(self, time, temp):
        self.schedules[time]=temp

    def __str__(self):
        result=f"Default temperature: {self.temp} degrees"
        for time in sorted(self.schedules):
            result+=f"\n{time} {self.schedules[time]} degrees"
        return result
    
    def get_target_temperature(self, time):
        total=None
        for t in sorted(self.schedules):
            if t<=time:
                total=t
            else:
                break

        if total is None:
            return self.temp
        return self.schedules[total]