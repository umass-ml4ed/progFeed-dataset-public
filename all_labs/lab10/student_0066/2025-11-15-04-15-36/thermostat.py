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
        
        line1 = f"Default temperature: {self.default_temp} degrees"
        
        other_lines = ""
        
        data = sorted(self.schedules)
        
        for time in data:
            temp = self.schedules[time]
            other_lines += f"\n{time} {temp} degrees"
            
            
            
        return line1 + other_lines
    
    
    
    def get_target_temperature(self, time):
        if not self.schedules:
            return self.default_temp
        
        data = sorted(self.schedules)
        
        searched = 0
        
        for t in data:
            if t <= time:
                searched = t
            else:
                break
            
        if searched == 0:
            return self.default_temp
        else:
            return self.schedules[searched]
        
        
        
dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
             