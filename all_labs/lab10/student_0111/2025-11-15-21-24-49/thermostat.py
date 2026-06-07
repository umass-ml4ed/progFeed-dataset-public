# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}   # empty dictionary, unique per object

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        # Start with the default temperature line
        result = f"Default temperature: {self.default_temp} degrees"

        # If no schedules, return this one line
        if len(self.schedules) == 0:
            return result

        # Otherwise, append sorted schedule lines
        sorted_times = sorted(self.schedules)
        for t in sorted_times:
            result += f"\n{t} {self.schedules[t]} degrees"

        return result

    def get_target_temperature(self, query_time):
        # Sort schedule times
        sorted_times = sorted(self.schedules)

        # If no schedules → return default
        if len(sorted_times) == 0:
            return self.default_temp

        # If query is before first scheduled time → default temp
        if query_time < sorted_times[0]:
            return self.default_temp

        # Track the latest valid time
        latest_time = None

        # Find the latest scheduled time <= query time
        for t in sorted_times:
            if t <= query_time:
                latest_time = t
            else:
                break

        # If we found a valid schedule time
        if latest_time is not None:
            return self.schedules[latest_time]

        # Fallback (shouldn't happen)
        return self.default_temp