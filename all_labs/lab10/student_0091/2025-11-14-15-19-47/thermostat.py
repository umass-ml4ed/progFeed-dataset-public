# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.schedule= {}
    def add_schedule(self, time:str, temperature:float):
        self.schedule[time]=temperature



