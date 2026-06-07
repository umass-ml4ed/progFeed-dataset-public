# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        result_lines = [f"Default temperature: {self.default_temp} degrees"]

        for t in sorted(self.schedules.keys()):
            result_lines.append(f"{t} {self.schedules[t]} degrees")

        return "\n".join(result_lines)

    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp

        sorted_times = sorted(self.schedules.keys())

        if query_time < sorted_times[0]:
            return self.default_temp

        latest_valid_time = None
        for t in sorted_times:
            if t <= query_time:
                latest_valid_time = t
            else:
                break

        if latest_valid_time is None:
            return self.default_temp

        return self.schedules[latest_valid_time]