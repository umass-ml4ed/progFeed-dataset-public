#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

class Thermostat:
    def __init__(self, default_temperature=68):
        self.default_temperature = default_temperature
        self.schedules = {}  

    def add_schedule(self, time: str, temperature: float):
        self.schedules[time] = temperature

    def __str__(self):
        string = f"Default temperature: {self.default_temperature} degrees"
        for time in sorted(self.schedules):
            temp = self.schedules[time]
            string += f"\n{time} {temp} degrees"
        return string

    def get_target_temperature(self, query_time:str):
        target_temp = self.default_temperature
        schedules = sorted(self.schedules)
        for time in schedules:
            if time <= query_time: 
                target_temp = self.schedules[time]
            else:
                break
        return target_temp
