# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        # Store the default temperature
        self.default_temp = default_temp

        # Make a new empty dictionary for schedules
        self.schedules = {}

    def add_schedule(self, time, temp):
        # Add or overwrite the time-temperature pair
        self.schedules[time] = temp

    def __str__(self):
        # Start with the default temperature line
        result = f"Default temperature: {self.default_temp} degrees"

        # If there are no schedules, stop here
        if len(self.schedules) == 0:
            return result

        # Get the times sorted in ascending order
        sorted_times = sorted(self.schedules)

        # Add each time-temperature line
        for t in sorted_times:
            result += f"\n{t} {self.schedules[t]} degrees"

        return result

    def get_target_temperature(self, query_time):
        # If no schedules at all → return default temp
        if len(self.schedules) == 0:
            return self.default_temp

        # Get sorted schedule times
        sorted_times = sorted(self.schedules)

        # Case 1: query time is earlier than the earliest schedule
        if query_time < sorted_times[0]:
            return self.default_temp

        # Case 2: find the latest schedule time <= query time
        last_time = sorted_times[0]  # start with earliest
        for t in sorted_times:
            if t <= query_time:
                last_time = t
            else:
                break

        return self.schedules[last_time]
