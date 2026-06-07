# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, dev=68):
        self.default_temp = dev
        self.schedules = {}
        
    def add_schedule(self, time: str, temp: float):
        self.schedules[time] = temp

    def __str__(self):
        # Start with default temperature line
        result = f"Default temperature: {self.default_temp} degrees"

        # No schedules → return only that line
        if not self.schedules:
            return result

        # Add schedules in sorted time order
        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"

        return result

    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp

        sorted_times = sorted(self.schedules)

        # If before the first schedule → default temp
        if query_time < sorted_times[0]:
            return self.default_temp

        # Latest time <= query_time
        latest_time = None
        for t in sorted_times:
            if t <= query_time:
                latest_time = t
            else:
                break

        if latest_time is not None:
            return self.schedules[latest_time]

        return self.default_temp
      