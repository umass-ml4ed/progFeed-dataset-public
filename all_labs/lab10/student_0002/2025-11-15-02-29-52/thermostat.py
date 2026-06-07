
# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp=68):
        self.default_temp = temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees\n"
        for time in sorted(self.schedules):
            result += f"{time} {self.schedules[time]} degrees\n"
        return result.strip()

    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp

        times = sorted(self.schedules)
        if query_time < times[0]:
            return self.default_temp

        for i in range(len(times)):
            if times[i] > query_time:
                return self.schedules[times[i - 1]]
        return self.schedules[times[-1]]