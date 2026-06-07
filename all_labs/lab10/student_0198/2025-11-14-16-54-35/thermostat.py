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
        if not self.schedule:
            return f"Default temperature: {self.temp} degrees"
        lines = [f"Default temperature: {self.temp} degrees"]
        for t in sorted(self.schedule):
            lines.append(f"{t} {self.schedule[t]} degrees")
        return "\n".join(lines)

    def get_target_temperature(self, time: str) -> float:

        last_temp = None
        for t in sorted(self.schedule):
            if t <= time:
                last_temp = self.schedule[t]
            else:
                break
        return last_temp if last_temp is not None else self.temp

    def get_target_temperatures(self, time: str) -> float:
        return self.get_target_temperature(time)