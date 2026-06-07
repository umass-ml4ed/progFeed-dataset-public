# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

def add_schedule(self, time, temperature):
    self.schedules[time] = temperature


def __str__(self):
    result = f'Default temperature: {self.default_temp} degrees\n'
    sorted_times = sorted(self.schedules)
    for i, time in enumerate(sorted_times):
        result += f'{time} {self.schedules[time]} degrees'
        if i < len(sorted_times) - 1:
            result += '\n'
    return result

def get_target_temperature(self, query_time):
    sorted_times = sorted(self.schedules)
    target_temp = self.default_temp

    for time in sorted_times:
        if query_time >= time:
            target_temp = self.schedules[time]
        else:
            break

    return target_temp