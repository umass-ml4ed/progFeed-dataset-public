# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, default_temp = 68):
        self.curr_temp = default_temp
        self.schedules = {}
    def add_schedule(self, time, newtemp):
        self.schedules[f'{time}'] = f'{newtemp}'
    def __str__(self):
        return str(f"Default temperature: {self.curr_temp} degrees")
        return str(sorted(self.schedules))
print(Thermostat())        
        
    