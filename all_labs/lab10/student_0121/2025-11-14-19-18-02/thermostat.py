# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, default_temp=68): #constructor 
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temperature): #stores time-temperature pair
        self.schedules[time] = temperature
    
    def __str__(self): #returns a string
        str = f"Default temperature: {self.default_temp} degrees"
        if not self.schedules:
            return str
        str += "\n"
        times = sorted(self.schedules)
        lines = []
        for time in times:
            temp = self.schedules[time]
            lines.append(f"{time} {temp} degrees")
        str += "\n".join(lines)
        return str
    
    def get_target_temperature(self, query_time): #returns the temperature 
        if not self.schedules:
            return self.default_temp
        times = sorted(self.schedules)
        target = None
        for time in times:
            if time <= query_time:
                target = time
            else:
                break
        if target is None:
            return self.default_temp
        else:
            return self.schedules[target]