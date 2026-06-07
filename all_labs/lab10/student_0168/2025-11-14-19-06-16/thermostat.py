# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
class Thermostat:
    def __init__(self, temperature=68):
        self.dev= temperature
        self.schedule={}
    def add_schedule(self, time, temperature):
        self.schedule[time]=temperature
    def __str__(self):
        res= f"Default temperature: {self.dev} degrees"
        if len(self.schedule)==0:
            return res
        list=sorted(self.schedule)
        for times in list:
            temperature= self.schedule[times]
            res+= f"\n{times} {temperature}"
        return res

print(Thermostat())
