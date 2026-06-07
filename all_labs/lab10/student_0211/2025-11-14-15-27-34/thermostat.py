# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp = 68):
        self.default_temp = default_temp
        self.schedules = {}
    def add_schedule(self, time, temprature):
        self.schedules[time] = float(temprature)
    def __str__(self):
        output = ""
        if len(self.schedules == 0):
            output += 'Default temprature: ' + str(self.temprature) + ' degrees'
        for time in sorted(self.schedules):
            output += f'\n {time} {self.schedules[time]} degrees'
        return output
    # def get_target_temprature(self, query):
    #     sort_time = sorted(self.schedules)

