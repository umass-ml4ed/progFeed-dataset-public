# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat():
    def __init__(self, default_temp=68):
        self.default_temperature = default_temp
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[str(time)] = float(temp)
    
    def __str__(self):
        result = f"Default temperature: {self.default_temperature} degrees"
        if self.schedules == {}:
            return result
        for key in sorted(self.schedules):
            temp = self.schedules[key]
            result += f"\n{key} {temp} degrees"
        return result

    def get_target_temperature(self, query_time):
        if self.schedules == {}:
            return self.default_temperature
        time = sorted(self.schedules)
        if query_time < time[0]:
            return self.default_temperature
        for hour in time:
            if hour <= query_time:
                latest_time = hour
            else:
                break
        if latest_time == None:
            return self.default_temperature
        return self.schedules[latest_time]


