# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp
    
    def __str__(self):
        output = "Default temperature: " + str(self.default_temp) + " degrees"
        
        if len(self.schedules) == 0:
            return output
        
        sorted_times = sorted(self.schedules)
        
        for time in sorted_times:
            temp = self.schedules[time]
            output += "\n" + time + " " + str(temp) + " degrees"
        
        return output
    
    def get_target_temperature(self, query_time):
        if len(self.schedules) == 0:
            return self.default_temp
        
        sorted_times = sorted(self.schedules)
        latest_time_before = None
        
        for time in sorted_times:
            if time <= query_time:
                latest_time_before = time
            else:
                break

        if latest_time_before is None:
            return self.default_temp

        return self.schedules[latest_time_before]
