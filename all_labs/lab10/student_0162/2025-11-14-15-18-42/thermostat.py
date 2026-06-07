# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temperature = 68):
        self.temperature = temperature
        self.schedules = {}

    def add_schedule(self,time:str,temp:float):
        self.schedules[time] = temp

    def __str__(self):
        sorts = sorted(self.schedules)
        a = [f"Default temperature: {self.temperature} degrees"]
        for time in sorts:
            temp = self.schedules[time]
            a.append(f"{time} {temp} degrees")
        return "\n".join(a)

    def get_target_temperature(self, query_time:str):
        target_temp = self.temperature
        sorts = sorted(self.schedules)
        for schedule_time in sorts:
            if schedule_time <= query_time:
                target_temp = self.schedules[schedule_time]
            else:
                break
        return target_temp 