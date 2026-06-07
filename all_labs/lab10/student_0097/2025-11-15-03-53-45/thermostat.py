# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#Exercise #1-3 
'''
class Thermostat:
    def __init__(self, default_T):
        self.default_T = default_T
        if default_T == None:
            default_T = 68
    #Gotta change the name on this one 
    def __str__(self, schedule):
        dict = {}
        schedule.append(dict)
    
    def add_schedule(self, time_str, temp_flt):
        self.time_str = time_str
        self.temp_flt = temp_flt
        time_str.append(dict)
        temp_flt.append(dict)
    
    def __str__(self,) '''

class Thermostat:
    def __init__(self, default_T=68):
        # store default temperature
        self.default_T = default_T
        # empty dictionary for schedules
        self.schedules = {}

    def add_schedule(self, time_str, temp_flt):
        # store time: temperature pair in the dictionary
        self.schedules[time_str] = temp_flt

    def __str__(self):
        # start with default line
        result = f"Default temperature: {self.default_T} degrees"

        # if there are schedules, add them sorted
        for time in sorted(self.schedules):
            temp = self.schedules[time]
            result += f"\n{time} {temp} degrees"

        return result

    def get_target_temperature(self, query_time):
        # sorted list of all times
        times = sorted(self.schedules)

        # if no times exist → return default
        if len(times) == 0:
            return self.default_T

        # if query is earlier than first schedule
        if query_time < times[0]:
            return self.default_T

        # find latest time <= query time
        target_time = times[0]
        for t in times:
            if t <= query_time:
                target_time = t

        return self.schedules[target_time]