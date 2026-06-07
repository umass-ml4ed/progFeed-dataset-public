# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp     
        self.schedules = {}            

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        lines = [f"Default temperature: {self.default_temp} degrees"]

        for time in sorted(self.schedules):
            temp = self.schedules[time]
            lines.append(f"{time} {temp} degrees")
        return "\n".join(lines)

    def get_target_temperature(self, query_time):
        if not self.schedules:
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