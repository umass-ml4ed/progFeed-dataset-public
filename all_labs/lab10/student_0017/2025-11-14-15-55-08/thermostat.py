# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:

    def __init__(self, default_temp=68):
        # store the default temperature
        self.default_temp = default_temp
        # create the dictionary for schedules
        self.schedules = {}

    def add_schedule(self, time, temp):
        # store the time-temperature pair in the dictionary
        self.schedules[time] = temp

    def __str__(self):
        # list to hold each line of the output
        lines = []
        lines.append(f"Default temperature: {self.default_temp} degrees")

        # sorted times
        for t in sorted(self.schedules):
            lines.append(f"{t} {self.schedules[t]} degrees")

        # join with newline (NO extra newline at the end)
        return "\n".join(lines)

    def get_target_temperature(self, query_time):
        # start with default
        target = self.default_temp

        # go through sorted schedule times
        for t in sorted(self.schedules):
            if t <= query_time:
                target = self.schedules[t]
            else:
                break

        return target

