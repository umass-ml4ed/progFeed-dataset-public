# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, tempurature=68):
        self.temp = tempurature
        self.schedule = {}
    def add_schedule(self, time, tempurature):
        self.schedule[time] = tempurature
    def __str__(self):
        msg = f'Default temperature: {self.temp} degrees'
        for t in self.schedule:
           msg += f'{t} {self.schedule[t]} degrees'
        return msg

    def get_target_temperature(self, q_time):
        target = None
        for t in self.schedule:
            if t <= q_time and (target is None or t > target):
                target = t
        return self.schedule[target] if target else self.temp
