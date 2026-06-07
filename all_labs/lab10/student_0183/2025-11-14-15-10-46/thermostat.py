# Author: REDACTED
# Email: REDACTED
# SpireID: REDACTED



class Thermostat:
    def __init__(self, default_temp=68):
        # Store default temperature
        self.default_temp = default_temp
        # Dictionary to store schedules: {time_str : temperature}
        self.schedules = {}

    def add_schedule(self, time, temperature):
        # Add or overwrite the schedule
        self.schedules[time] = temperature

    def __str__(self):
        # First line: default temperature
        result = f"Default temperature: {self.default_temp} degrees"

        # If no schedules, return just the first line
        if len(self.schedules) == 0:
            return result

        # Append sorted schedule entries
        for time in sorted(self.schedules):
            temp = self.schedules[time]
            result += f"\n{time} {temp} degrees"

        return result

    def get_target_temperature(self, query_time):
        # If no schedules exist, return default temperature
        if len(self.schedules) == 0:
            return self.default_temp

        # Find all schedule times <= query_time
        valid_times = [t for t in self.schedules if t <= query_time]

        if len(valid_times) == 0:
            # Query time is earlier than all scheduled times
            return self.default_temp

        # Find the latest applicable schedule
        latest_time = max(valid_times)
        return self.schedules[latest_time]