# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, defaultTemp=68):
        self.defaultTemp = defaultTemp
        self.schedules = {}
    
    def add_schedule(self,time,temp):
        self.schedules[time] = temp

    def __str__(self):
        string = f"Default temperature: {self.defaultTemp} degrees"
        for time in sorted(self.schedules):
                string += f"\n{time} {self.schedules[time]} degrees"
        return string
    
    def get_target_temperature(self,querytime):
        sortedtimes = sorted(self.schedules)
        targettemp = self.defaultTemp
        for time in sortedtimes:
            if querytime >= time:
                targettemp = self.schedules[time]
            else:
                break
        return targettemp
