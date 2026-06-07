# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, tempurature = 68,):
        self.temp = tempurature
        self.schedule = {}
    def add_schedule(self, time, tempurature):
        self.schedule[time] = tempurature
    def __str__(self):
        for t in self.schedule:
            msg = f'Default temperature: {self.temp} degrees'

            txt += f'\n{t} {self.schedule[t]} degrees'
        return msg