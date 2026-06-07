# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        lines = [f"Default temperature: {self.default_temp} degrees"]
        sorted_times = sorted(self.schedules.keys())
        for t in sorted_times:
            temp = self.schedules[t]
            lines.append(f"{t} {temp} degrees")
        return "\n".join(lines)

    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp
        sorted_times = sorted(self.schedules.keys())
        latest_time = None
        for t in sorted_times:
            if t <= query_time:
                latest_time = t
            else:
                break
        if latest_time is None:
            return self.default_temp
        else:
            return self.schedules[latest_time]