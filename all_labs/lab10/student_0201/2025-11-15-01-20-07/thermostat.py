# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedule = {}
        
    def add_schedule(self, time,temp):
        self.schedule[time] = temp

    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"
        for time in sorted(self.schedule):
            result += f"\n{time} {self.schedule[time]} degrees"
        return result
        
    def get_target_temperature(self, query_t):
        times = sorted(self.schedule)
        if not times:
            return self.default_temp
        if query_t<times[0]:
            return self.default_temp
        last_t = None
        for time in times:
            if time <= query_t:
                last_t = time
            else:
                break
        if last_t is not None:
            return self.schedule[last_t]
        return self.default_temp