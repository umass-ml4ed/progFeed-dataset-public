# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp=68):
        self.defaulttemp = temp
        self.schedules = {}
    def add_schedule(self, time, temp):
        self.schedules[time] = temp
    def __str__(self):
        response = f'Default temperature: {self.defaulttemp} degrees'
        if not self.schedules:
            return response
        else:
            for time in sorted(self.schedules):
                temp = self.schedules[time]
                response += f'\n{time} {temp} degrees'
            return response
    def get_target_temperature(self, time):
        if not self.schedules:
            return self.defaulttemp
        times = sorted(self.schedules)
        latest_time = None
        for time in times:
            if time <= time:
                latest_time = time
            else:
                break
        if latest_time is None:
            return self.defaulttemp
        return self.schedules[latest_time]
        



#TEST CODE DELETE AFTER

dev = Thermostat(75)

dev.addschedule("8:00", 65)

print(dev)