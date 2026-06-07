# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

class Thermostat:
    
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {} 

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"

        if len(self.schedules) == 0:
            return result

        for time in sorted(self.schedules):
            temp = self.schedules[time]
            result += f"\n{time} {temp} degrees"

        return result

    def get_target_temperature(self, query_time):
        times = sorted(self.schedules)

        if len(times) == 0:
            return self.default_temp

        if query_time < times[0]:
            return self.default_temp

        latest_time = None
        for t in times:
            if t <= query_time:
                latest_time = t
            else:
                break

        if latest_time is not None:
            return self.schedules[latest_time]

        return self.default_temp