# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, def_temperature = 68):
        self.def_temperature = def_temperature
        self.schedule = {}
    
    def add_schedule(self, time:str, temperature:float):
        self.schedule[time] = temperature
    
    def __str__(self):
        sorted_schedule = sorted(self.schedule)
        strings = f"Default temperature: {self.def_temperature} degrees"
        for time in sorted_schedule:
            temperature = self.schedule[time]
            strings += f"\n{time} {temperature} degrees"
        return strings
    
    def get_target_temperature(self, query_time:str):
        sorted_time = sorted(self.schedule.keys())
        target_temperature = self.def_temperature
        for schedule_times in sorted_time:
            if schedule_times <= query_time:
                target_temperature = self.schedule[schedule_times]
            else:
                break
        return target_temperature