# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__ (self, temperature=68):
        self.temperature = temperature
        self.schedule = {}
    def add_schedule (self, time, temp):
        self.schedule[time] = temp
    def __str__ (self):
        first_line = f"Default temperature: {self.temperature} degrees" 
        for time in sorted(self.schedule):
            temp = self.schedule[time]
            first_line += f"\n{time} {temp} degrees"
        return first_line
    def get_target_temperature (self, query_time):
        last_temp = self.temperature 
        for time in sorted(self.schedule):
            if time <= query_time:
                last_temp = self.schedule[time]
            else:
                break
        if last_temp == self.temperature and self.schedule:
            last_time = sorted(self.schedule)[-1]
            last_temp = self.schedule[last_time]
        return last_temp