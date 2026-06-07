# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED




class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}
        
        
        
    def add_schedule(self, time, temperature):
        
        self.schedules[time] = temperature
        
        
    def __str__(self):
        
        line1 = f"Default temperature: {self.default_temp}\n"
        
        other_lines = ""
        
        data = sorted(self.schedules)
        
        for time in data:
            temp = self.schedules[time]
            other_lines.append(f"{time} {temp} degrees \n")
            
            
        return line1 + other_lines
        
        
        
        
        