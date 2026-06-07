# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temperature=68):
        self.temperature = temperature
        self.schedules = {}  
    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature
    def __str__(self):
        string = f"Default temperature: {self.temperature} degrees"
        if not self.schedules:
            return string
        sorted_times = sorted(self.schedules)
        for time in sorted_times:
            temp = self.schedules[time]
            string += f"\n{time} {temp} degrees"
        return string
    def get_target_temperature(self,time):
        if not self.schedules:
            return self.temperature
        sorted_times = sorted(self.schedules)
        if time < sorted_times[0]:
            return self.temperature
        last_time = sorted_times[0]   
        for t in sorted_times:
            if t <= time:
                last_time = t
            else:
                break
        return self.schedules[last_time]

