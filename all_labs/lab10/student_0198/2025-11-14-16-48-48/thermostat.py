# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
class Thermostat:
    def __init__(self, temp:int=68):
        if temp is False:
            temp = 68    
        self.temp =temp
        self.schedule = {}
    def add_schedule(self, time:str, temp:float):
        self.schedule[time]=temp
    def __str__(self):
        default_temp = self.temp
        lines = []
        for time in sorted(self.schedule):
            lines.append(f"\n{time} {self.schedule[time]} degrees")
        if len(lines)>0:
            return f"Default temperature: {default_temp} degrees{lines}"
        else:
            return f"Default temperature: {default_temp} degrees"
    def get_target_temperatures(self, time:str):
        self.nschedule = sorted(self.schedule)
        for i in self.nschedule:
            if time>i:
                continue
            else:
                return self.nschedule[i]