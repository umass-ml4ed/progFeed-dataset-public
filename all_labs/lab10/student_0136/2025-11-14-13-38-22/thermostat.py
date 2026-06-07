# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat: 

    def __init__(self, default=68):
        self.default = default
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        final = [f"Default temperature: {self.default} degrees"]
        lst = sorted(self.schedules)
        for time in lst:
            temp = self.schedules[time]
            final.append(f"{time} {temp} degrees")
        return "\n".join(final)

    def get_target_temperature(self, q_time):
        hours, minutes = q_time.split(":")
        q_val = (int(hours) * 100) + int(minutes)
        if not self.schedules:
            return self.default
        lst = sorted(self.schedules)
        latest = self.default
        for time in lst:
            t_hours, t_minutes = time.split(":")
            t_val = (int(t_hours) * 100) + int(t_minutes)
            if t_val <= q_val:
                latest = self.schedules[time]
            else:
                break
        return latest
        