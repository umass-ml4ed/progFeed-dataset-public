# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
class Thermostat:
    def __init__(self, temp: int = 68):
        if temp is False:
            temp = 68
        self.temp = temp
        self.schedule = {}

    def add_schedule(self, time: str, temp: float):
        self.schedule[time] = temp

    def __str__(self):
        default_temp = self.temp
        if not self.schedule:
            return f"Default temperature: {default_temp} degrees"
        lines = [f"Default temperature: {default_temp} degrees"]
        for time in sorted(self.schedule):
            lines.append(f"{time} {self.schedule[time]} degrees")
        return "\n".join(lines)

    def get_target_temperature(self, time: str):
        for t in sorted(self.schedule):
            if time <= t:
                return self.schedule[t]
        return self.temp