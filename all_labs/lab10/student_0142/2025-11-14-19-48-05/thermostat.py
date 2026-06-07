# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#1
class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}   
#2
    def add_schedule(self, time, temp):
        self.schedules[time] = temp
#3
    def __str__(self):
       
        result = f"Default temperature: {self.default_temp} degrees"
        if len(self.schedules) == 0:
            return result

       
        for time in sorted(self.schedules):
            temp = self.schedules[time]
            result += f"\n{time} {temp} degrees"

        return result

#4
    def get_target_temperature(self, query_time):
        if len(self.schedules) == 0:
            return self.default_temp

        times = sorted(self.schedules)

        if query_time < times[0]:
            return self.default_temp

        latest_time = None
        for t in times:
            if t <= query_time:
                latest_time = t
            else:
                break

        if latest_time is None:
            return self.default_temp

        return self.schedules[latest_time]

#5
class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}   # empty dict for time→temp

    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"

        if len(self.schedules) == 0:
            return result

        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"

        return result

    def get_target_temperature(self, query_time):
        if len(self.schedules) == 0:
            return self.default_temp

        times = sorted(self.schedules)

        if query_time < times[0]:
            return self.default_temp

        latest_time = None
        for t in times:
            if t <= query_time:
                latest_time = t
            else:
                break

        if latest_time is None:
            return self.default_temp

        return self.schedules[latest_time]
