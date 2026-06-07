# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temperature=68):
        self.default_temperature = default_temperature
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        result = f"Default temperature: {self.default_temperature} degrees"
        sorted_times = sorted(self.schedules)

        for time in sorted_times:
            temp = self.schedules[time]
            result += f"\n{time} {temp} degrees"

        return result
    
    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temperature

        sorted_times = sorted(self.schedules)

        if query_time < sorted_times[0]:
            return self.default_temperature

        last_time = None
        for time in sorted_times:
            if time <= query_time:
                last_time = time
            else:
                break

        if last_time is not None:
            return self.schedules[last_time]

        return self.default_temperature