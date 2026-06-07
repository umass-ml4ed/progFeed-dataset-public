# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat():
    def __init__(self, n = 68):
        self.n = n
        self.schedules = {}

    def add_schedule(self,time:str, temp:float):
        self.schedules[time] = temp

    def __str__(self):
        result = f"Default temperature: {self.n} degrees"

        if not self.schedules:
            return result
        
        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"
        return result 
    
    def get_target_temperature(self, query_time: str):
        if not self.schedules:
            return self.n

        times = sorted(self.schedules)

        if query_time < times[0]:
            return self.n

        last_valid_temp = None

        for t in times:
            if t <= query_time:
                last_valid_temp = self.schedules[t]
            else:
                break 

        if last_valid_temp is not None:
            return last_valid_temp
        return self.n