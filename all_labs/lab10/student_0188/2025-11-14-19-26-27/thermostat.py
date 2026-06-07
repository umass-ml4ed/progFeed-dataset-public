# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        """
        Constructor.
        Creates a thermostat with a default temperature and
        an empty schedule dictionary.
        """
        self.default_temp = default_temp
        self.schedules = {}   # MUST be a new dictionary for every object

    def add_schedule(self, time, temperature):
        """
        Adds or updates a schedule entry.
        time: string in 'HH:MM'
        temperature: float
        """
        self.schedules[time] = temperature

    def __str__(self):
        """
        Returns a formatted string showing the default temperature
        and all schedules sorted in ascending order of time.
        """
        result = f"Default temperature: {self.default_temp} degrees"

        # If no schedules exist, return just the default line
        if len(self.schedules) == 0:
            return result

        # Append each schedule in sorted order
        for time in sorted(self.schedules):
            temp = self.schedules[time]
            result += f"\n{time} {temp} degrees"

        return result

    def get_target_temperature(self, query_time):
        """
        Returns the temperature at the given time.
        Uses the most recent schedule <= query_time.
        If none exists, return the default temperature.
        """
        if len(self.schedules) == 0:
            return self.default_temp

        # Sort all schedule times
        sorted_times = sorted(self.schedules)

        # If query time is earlier than the first schedule
        if query_time < sorted_times[0]:
            return self.default_temp

        # Otherwise find the latest time <= query_time
        latest_time = sorted_times[0]
        for t in sorted_times:
            if t <= query_time:
                latest_time = t
            else:
                break

        return self.schedules[latest_time]
