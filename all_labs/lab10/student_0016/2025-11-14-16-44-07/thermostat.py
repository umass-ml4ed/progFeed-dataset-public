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
        sch_str = ""
        for time in sorted(self.schedule):
            sch_str += f"\n{time} {self.schedule[time]} degrees"
        return (f"Default temperature: {self.temp} degrees" + sch_str)

    def get_target_temperature(self, targ_time):
        for time in sorted(self.schedule)[::-1]:
            if time <= targ_time:
                return self.schedule[time]
        return self.temp