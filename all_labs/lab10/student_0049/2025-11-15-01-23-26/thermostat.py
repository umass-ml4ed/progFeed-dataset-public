# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

# thermostat.py

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedule = {}

    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature
    
    def __str__(self):
        lines = [f"Default temperature: {self.default_temp} degrees"]
        for time in sorted(self.schedule):
            lines.append(f"{time} {self.schedule[time]} degrees")
        return '\n'.join(lines)
    def get_target_temperature(self, query_time):
        if not self.schedule:
            return self.default_temp

        sorted_times = sorted(self.schedule)
        for time in reversed(sorted_times):
            if time <= query_time:
                return self.schedule[time]
        return self.default_temp

