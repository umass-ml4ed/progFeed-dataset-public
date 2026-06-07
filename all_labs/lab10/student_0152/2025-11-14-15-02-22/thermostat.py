# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp = 68):
        self.temp = temp
        self.temps = {}
    def add_schedule(self, time, temp):
        self.temps[time] = temp
    def __str__(self):
        sort = [f'Default temperature: {self.temp}']
        for time in sorted(self.temps): 
            sort.append(f'{time} {self.temps[time]} degrees')
        return '\n'.join(sort)