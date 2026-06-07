# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, tempurature=68):
        self.temp = tempurature
        self.schedule = {}
    def add_schedule(self, time, tempurature):
        self.schedule[time] = tempurature
    def get_target_temperature(self, time):
        return self.schedule.get(time, self.temp)
    def __str__(self):
        msg = f'Default temperature: {self.temp} degrees'
        for t in self.schedule:
            msg += f'\n{t} {self.schedule[t]} degrees'
        return msg
