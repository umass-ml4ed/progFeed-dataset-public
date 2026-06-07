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
        best_time = None
        for time in sorted(self.schedule):
            if time <= query_time:
                best_time = time
            else:
                break
        if best_time is None:
            return self.temperature
        return self.schedule[best_time]