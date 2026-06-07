# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedule= {}
    def add_schedule(self, time:str, temperature:float):
        self.schedule[time]=temperature

    def __str__(self):
        result=f"Default temperature: {self.default_temp} degrees"
        sorted_times=sorted(self.schedule)

        if len(sorted_times)==0:
            return result

        for time in sorted_times:
            temp = self.schedule[time]
            result += f"\n{time} {temp} degrees"

        return result

def get_target_temperature(self, query_time):

    sorted_times = sorted(self.schedule)
    latest_time = None

    for time in sorted_times:
        if time <= query_time:
            latest_time = time

    if latest_time is None:
        return self.default_temp

    return self.schedule[latest_time]


print(Thermostat())











