# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat():
    def __init__(self, default_temp = 68):
        self.default_temperature = default_temp
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[str(time)] = float(temp)
    
    def __str__(self):
        list = ""
        if self.schedules == {}:
            return (f"Default temperature: {self.default_temperature} degrees")
        for key in self.schedules:
            temp = self.schedules[key]
            list += f"{key} {temp} degrees\n"
        return (f"Default temperature: {self.default_temperature} degrees\n{list}")
    
#    def get_target_temperature(query_time):
#        return self.schedule[query_time]


