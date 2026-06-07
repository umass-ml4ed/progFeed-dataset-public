# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temperature=68):
        self.temperature=temperature
        self.schedule={}
    def add_schedule(self,time,tempr):
        self.schedule[time]=tempr
    def __str__(self):
        temp=f"Default temperature: {self.temperature} degrees"
        if not self.schedule:
            return temp
        for time in sorted(self.schedule):
            tempr=self.schedule[time]
            temp+=f"\n{time} {tempr} degrees"
        return temp
    def get_target_temperature(self,query_time):
        if not self.schedule:
            return f"Default temperature: {self.temperature} degrees"
        sched=sorted(self.schedule)
        if query_time<sched[0]:
            return f"Default temperature: {self.temperature} degrees"
        latesttime=sched[0]
        for t in sched:
            if t <= query_time:
                latesttime=t
            else:
                return self.schedules[latesttime]

