# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def _to_minutes(self, time):
        h, m = map(int, time.split(":"))
        return h * 60 + m

    def get_target_temperature(self, time):
        current_time = self._to_minutes(time)

        valid_times = [
            t for t in self.schedules
            if self._to_minutes(t) <= current_time
        ]

        if not valid_times:
            return self.default_temp

        latest_time = max(valid_times, key=self._to_minutes)
        return self.schedules[latest_time]
    
    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"

        for time in sorted(self.schedules, key=self._to_minutes):
            result += f"\n{time} {self.schedules[time]} degrees"

        return result
