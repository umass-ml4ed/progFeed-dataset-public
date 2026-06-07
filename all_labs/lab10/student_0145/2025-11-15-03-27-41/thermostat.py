# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat: 

    def __init__(self, default_temperature = 68):

        self.default_temperature = default_temperature 

        self.schedules = {}

    def add_schedule(self,time,temperature): 
        
        self.schedules[time] = temperature

    def __str__(self):
        result = f"Default temperature: {self.default_temperature} degrees"

        if not self.schedules:
            return result

        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"

        return result

    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temperature

        latest_time = None

        for time in sorted(self.schedules):
            if time <= query_time:
                latest_time = time
            else:
                break

        if latest_time is None:
            return self.default_temperature

        return self.schedules[latest_time]




   