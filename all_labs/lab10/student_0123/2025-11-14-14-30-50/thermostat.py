# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default=68):
        self.default = default
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp
    
    def __str__(self):
        sorted_times = sorted(self.schedules)   # list of sorted keys
        sorted_schedule = ""
        for time in sorted_times:
            temp = self.schedules[time]
            sorted_schedule += f"\n{time} {temp} degrees"
        return f"Default temperature: {self.default} degrees{sorted_schedule}"
    
    def get_target_temperature(self, query_time):
        sorted_times = sorted(self.schedules.keys())
        if not sorted_times:
            return self.default
        if query_time < sorted_times[0]:
            return self.default
        last_time = None
        for time in sorted_times:
            if time <= query_time:
                last_time = time
            else:
                break
        if last_time is not None:
            return self.schedules[last_time]
        return self.default