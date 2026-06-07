# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temperature=68):
        # default temperature
        self.temperature = temperature
        # schedules: time (str) -> temperature (float)
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        # First line: default temperature
        result = f"Default temperature: {self.temperature} degrees"

        # If no schedules, return just that line
        if len(self.schedules) == 0:
            return result

        # Otherwise, append each schedule in sorted time order
        for time in sorted(self.schedules):
            degree = self.schedules[time]
            result += f"\n{time} {degree} degrees"

        return result

    def get_target_temperature(self, query_time):
        # No schedules: always default temperature
        if not self.schedules:
            return self.temperature

        # Sorted times
        times = sorted(self.schedules)

        # If query time is earlier than first schedule
        if query_time < times[0]:
            return self.temperature

        # Find latest time <= query_time
        target_temp = self.schedules[times[0]]
        for t in times:
            if t <= query_time:
                target_temp = self.schedules[t]
            else:
                break

        return target_temp









