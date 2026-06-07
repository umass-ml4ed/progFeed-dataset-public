# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, dtemp = 68):
        self.dtemp = dtemp
        self.sched = {}
    
    def add_sched(self, time, temp):
        self.sched[time] = temp

    def __str__(self):
        newsched = sorted(self.sched)
        text = f"Default temperature: {self.dtemp} degrees"
        for t in newsched:
            temp = self.sched[t]
            text += f"\n{t} {temp} degrees"
        return text
    
    def get_target_temperature(self, query_time):
        sorted_time = sorted(self.sched.keys())
        target_temp = self.dtemp
        for sched_time in sorted_time:
            if sched_time <= query_time:
                target_temp = self.sched[sched_time]
            else:
                break
        return target_temp














