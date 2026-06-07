# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp=68):
        self.temp = temp
        self.sched = {}
    def add_schedule(self, time, temperature):
        self.sched[time] = temperature
    def __str__(self):
        lines = [f"Default temperature: {self.temp} degrees"]
        for time in sorted(self.sched):
            lines.append(f"{time} {self.sched[time]} degrees")
        return "\n".join(lines)
    def get_target_temperature(self, time):
        times = sorted(self.sched)
        last_time = None
        for t in times:
            if t <= time:
                last_time = t
            else:
                break
        if last_time == None:
            return self.temp