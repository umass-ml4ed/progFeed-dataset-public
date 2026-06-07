# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostsat:
    def __init__(self, tempurature = 68,):
        self.temp = tempurature
        self.schedule = {}
    def add_schedule(self, time, tempurature):
        self.schedule[time] = tempurature
    def __str__(self):
         return f'Default temperature: {self.temp} degrees \n {time} {self.schedule[time]} degrees \n {time} {self.schedule[time]} degrees'