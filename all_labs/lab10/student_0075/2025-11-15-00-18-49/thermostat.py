# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp=68):
        self.temp = temp
        self.schedules = {}

    def __str__(self):
        lines = [f"Default temperature: {self.temp} degrees"]
        for time in sorted(self.schedules):
            temp2 = self.schedules[time]
            lines.append(f"{time} {temp2} degrees")
        return "\n".join(lines)

    def add_schedule(self, time, temp):
        self.schedules[time] = float(temp)

    def get_target_temperature(self, time):
        target_temp = self.temp
        for scheduled_time in sorted(self.schedules):
            if scheduled_time <= time:
                target_temp = self.schedules[scheduled_time]
            else:
                break
        return target_temp
