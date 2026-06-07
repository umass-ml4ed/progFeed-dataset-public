# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def __init__(self, default_temp=68):
    self.default_temp = default_temp
    self.schedules = {}



def add_schedule(self, time, temperature):
    self.schedules[time] = temperature



def __str__(self):
    result = f"Default temperature: {self.default_temp} degrees"
    for time in sorted(self.schedules):
        result += f"\n{time} {self.schedules[time]} degrees"
    return result



def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp
        times = sorted(self.schedules)
        if query_time < times[0]:
            return self.default_temp
        for i in range(len(times) - 1):
            if times[i] <= query_time < times[i + 1]:
                return self.schedules[times[i]]
        return self.schedules[times[-1]]