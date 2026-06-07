# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self,temp = 68):
        self.temperature = temp
        self.schedule = {}

    def add_schedule(self,time,temperature):
        self.schedule[time] = temperature

    def __str__(self):
        default_temp = "Default temperature: " + str(self.temperature) + " " + "degrees"
        sorted_schedule = sorted(self.schedule)
        new_time = ""
        for time in sorted_schedule:
            new_time += '\n' + time + " " + str(self.schedule[time]) + " " + "degrees"
        return default_temp + new_time
    
    def get_target_temperature(self,query_time):
        target = 2359
        target_time = ""
        for time in sorted(self.schedule):
            new_time = time[0:2] + time[3:]
            new_query_time = query_time[0:2] + query_time[3:]
            if int(new_query_time) - int(new_time) >= 0 and int(new_query_time) - int(new_time) < target:
                target = int(new_query_time) - int(new_time)
                target_time = time
            elif sorted(self.schedule).index(time) == len(sorted(self.schedule)) - 1:
                return self.temperature
            else:
                continue
        return self.schedule[target_time]

