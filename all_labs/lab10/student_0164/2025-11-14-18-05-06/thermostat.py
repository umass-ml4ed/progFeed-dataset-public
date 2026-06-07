# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

class thermostat:
    def __init__(self, default_temp=68):
        self.defualt_temp = default_temp
        self.schedules = {}
    
    
    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature 

    def __str__(self):
        lines = ['f"Default temperature: {self.default_temp} degrees']
        for time in sorted(self.schedules):
            lines.append(f"{time} {self.schedules[time]} degrees")
        return "\n".join(lines)
   
    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp
        times = sorted(self.schedules)
        last_temp = self.defualt_temp
        for t in times:
            if t <= query_time:
                last_temp = self.schedules[t]
            else:
                break
        return last_temp
    