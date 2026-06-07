# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}     # time → temperature dictionary

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        # start with default temperature line
        result = f"Default temperature: {self.default_temp} degrees"

        # if no schedules, return immediately (NO trailing newline)
        if len(self.schedules) == 0:
            return result

        # add a newline after default temp
        result += "\n"

        # sorted list of schedule times
        sorted_times = sorted(self.schedules)

        # build each schedule line
        lines = []
        for t in sorted_times:
            lines.append(f"{t} {self.schedules[t]} degrees")

        # join all schedule lines with newline, no extra newline at end
        result += "\n".join(lines)
        return result

    def get_target_temperature(self, query_time):
        # if no schedules exist → return default temperature
        if len(self.schedules) == 0:
            return self.default_temp

        # get sorted list of times
        sorted_times = sorted(self.schedules)

        # find the latest time ≤ query_time
        latest = None
        for t in sorted_times:
            if t <= query_time:
                latest = t
            else:
                break

        # if query_time is earlier than the first schedule
        if latest is None:
            return self.default_temp

        # otherwise return the scheduled temperature
        return self.schedules[latest]