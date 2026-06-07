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
        msg = f"Default temperature: {self.temp} degrees"
        for t in sorted(self.schedule):
            msg += f"\n{t} {self.schedule[t]} degrees"
        return msg

    def get_target_temperature(self, q_time):
        target_time = None
        for t in self.schedule:
            if t <= q_time and (target_time is None or t > target_time):
                target_time = t
        return self.schedule[target_time] if target_time else self.temp
