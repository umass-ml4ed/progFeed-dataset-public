#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

class Thermostat:
    data = {}
    def __init__(self,temp=68):
        self.temp = temp
        self.schedule = {}
    def add_schedule(self,time,temp):
        self.schedule[time] = temp

