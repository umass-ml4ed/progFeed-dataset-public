# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default = 68):
        self.default = default
        self.schedule = {}

    def add_schedule(self,time,temp):
        self.scheule[time] = temp

    def __str__(self):
        res = f"Default temperature: {self.default} degrees"
        if not self.schedule:
            return res
        res = res + "/n"
        sorted = sorted(self.schedule)
        lin = []
        for time in sorted:
            temp = self.schedule[time]
            lin.append(f"{time} {temp} degrees")
        res += "/n".join(lin)
        return res

    def get_target_temperature(self, query_time):
        sorted_times = sorted(self.schedule)
        last_time = None

        for time in sorted_times:
            if time <= query_time:
                last_time = time
            else:
                break
        if last_time is None:
            return self.default_temp
        else:
            return self.schedule[last_time]