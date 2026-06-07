# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat():
    def __init__(self, default_temp = 68, ):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = float(temperature)

    def __str__(self):
        proper_output = f"Default temperature: {self.default_temp} degrees"
        for time in sorted(self.schedules):
            proper_output += f"\n{time} {self.schedules[time]} degrees"
        return proper_output
    
    def get_target_temperature(self, query_time):
        increasing_times = sorted(self.schedules)
        largest_time = False
        for time in increasing_times:
            if time <= query_time:
                largest_time = time
        if largest_time == False:
            return self.default_temp
        return self.schedules[largest_time]
            





