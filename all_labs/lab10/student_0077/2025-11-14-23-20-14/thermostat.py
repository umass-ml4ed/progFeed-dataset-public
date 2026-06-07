# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
import math
import random

class Thermostat:
    def __init__(self, temp=68):
        self.temp= temp
        self.schedule={}
    
    def add_schedule(self, time, temp):
        self.schedule[time]= temp
    
    def __str__(self):
        out=[f'Default temperature: {self.temp} degrees']
        for time in sorted(self.schedule):
            out.append(f'{time} {self.schedule[time]} degrees')
        return '\n'.join(out)
    
    def get_target_temperature(self, query_time):
        sorted_time= sorted(self.schedule.keys())
        target_temp= self.temp
        for time in sorted_time:
            if time<= query_time:
                target_temp= self.schedule[time]
            else:
                break

        return target_temp