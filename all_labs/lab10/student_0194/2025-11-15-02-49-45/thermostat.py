# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temperature=68):
        self.temperature = temperature
        self.schedule = {}
        
    def add_schedule(self, time, temp):
        self.schedule[time] = temp
    
    def __str__(self):
        str = f'Default temperature: {self.temperature} degrees\n'
        ordered = sorted(self.schedule)
        for i in ordered:
            str += f'{i} {self.schedule[i]} degrees\n'
        str = str.strip()
        return str
    
    def get_target_temperature(self, qTime):
        sorted_times = list(sorted(self.schedule.keys()))
        tTemp = self.temperature
        for time in sorted_times:
            if (time <= qTime):
                tTemp = self.schedule[time]
            else:
                break
        return tTemp
