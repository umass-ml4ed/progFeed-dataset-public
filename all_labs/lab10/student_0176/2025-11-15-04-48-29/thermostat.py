# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.defaultTemp =default_temp
        self.Schedules = {}

    def add_schedule(self, time, temp):
        self.Schedules[time]= temp

    def __str__(self):
        outStr = f"Default temperature:{self.defaultTemp} degrees"
        if not self.Schedules:
            return outStr
        for t in sorted(self.Schedules):
            val = self.Schedules[t]
            outStr += "\n" + t + " " +str(val) +" degrees"
        return outStr

    def get_target_temperature(self, queryTime):
        if not self.Schedules:
            return self.defaultTemp
        timesList = sorted(self.Schedules)
        if queryTime <timesList[0]:
            return self.defaultTemp
        lastTime = None
        for t in timesList:
            if t<= queryTime:
                lastTime= t
            else:
                break
        if lastTime is None:
            return self.defaultTemp
        return self.Schedules[lastTime]
