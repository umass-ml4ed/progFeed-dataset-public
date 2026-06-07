# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}   # dictionary: time → temperature

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        # Start with default temperature line
        output = f"Default temperature: {self.default_temp} degrees"

        # If no schedules, just return the default line
        if not self.schedules:
            return output

        # Sort the dictionary keys (strings sort chronologically)
        sorted_times = sorted(self.schedules)

        # Append each schedule line
        for t in sorted_times:
            output += f"\n{t} {self.schedules[t]} degrees"

        return output

    def get_target_temperature(self, query_time):
        # If no schedules at all → return default
        if not self.schedules:
            return self.default_temp

        # Sorted list of schedule times
        sorted_times = sorted(self.schedules)

        # If query time is earlier than the earliest schedule → default
        if query_time < sorted_times[0]:
            return self.default_temp

        # Otherwise, find the most recent schedule time ≤ query_time
        latest_time = None
        for t in sorted_times:
            if t <= query_time:
                latest_time = t
            else:
                break

        # If none found (should not happen due to earlier check), return default
        if latest_time is None:
            return self.default_temp

        return self.schedules[latest_time]